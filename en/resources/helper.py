from machine import Pin, PWM
import time, network, ujson as json, urequests as requests, errno

# ---------- Colours ----------
colours = {
    "off": (0, 0, 0),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "yellow": (255, 255, 0),
    "white": (255, 255, 255),
}


# ---------- LED ----------
class LED:
    def __init__(self, r, g, b, default="off"):
        self._r = PWM(Pin(r), freq=1000)
        self._g = PWM(Pin(g), freq=1000)
        self._b = PWM(Pin(b), freq=1000)
        self.on(default)

    def _set_rgb(self, r, g, b):
        # Map 0-255 to 0-1023 for ESP32 PWM
        self._r.duty(int(r * 4.0117))
        self._g.duty(int(g * 4.0117))
        self._b.duty(int(b * 4.0117))

    def on(self, name_or_tuple):
        if isinstance(name_or_tuple, str):
            r, g, b = colours.get(name_or_tuple, colours["off"])
        else:
            r, g, b = name_or_tuple
        self._set_rgb(r, g, b)

    def off(self):
        self.on("off")

    def blink(self, colour="white", seconds=0.3):
        self.on(colour)
        time.sleep(seconds)
        self.off()


# ---------- Wi-Fi ----------
class WiFi:
    @staticmethod
    def connect(ssid, password, on_success=None):
        sta = network.WLAN(network.STA_IF)
        if not sta.active():
            sta.active(True)
        if not sta.isconnected():
            sta.connect(ssid, password)
            # Try until connected
            while not sta.isconnected():
                time.sleep(0.2)
        if on_success:
            on_success()
        return sta


# ---------- TouchPads ----------
class Touchpad:
    """Simple debounced input for a touch pin."""

    def __init__(self, pin, active_high=True, debounce_ms=150):
        self.pin = Pin(pin, Pin.IN)
        self.active = 1 if active_high else 0
        self.debounce_ms = debounce_ms
        self._last_val = self.pin.value()
        self._last_change = time.ticks_ms()
        self._latched_touch = False

    def touched(self):
        """Returns True once per distinct touch."""
        now = time.ticks_ms()
        val = self.pin.value()
        if val != self._last_val:
            if time.ticks_diff(now, self._last_change) > self.debounce_ms:
                self._last_change = now
                if val == self.active and self._last_val != self.active:
                    self._latched_touch = True
            self._last_val = val
        if self._latched_touch:
            self._latched_touch = False
            return True
        return False


# ---------- ntfy ----------
class Ntfy:
    def __init__(self, topic, server="http://ntfy.sh", token=None):
        self.server = server.rstrip("/")
        self.topic = topic
        self.token = token
        self._resp = None
        self._last_seen = (0, "")
        self._open_stream()

    def _auth_header(self):
        if not self.token:
            return None
        return (
            self.token
            if self.token.lower().startswith("bearer ")
            else "Bearer " + self.token
        )

    def _open_stream(self):
        url = "{}/{}/json".format(self.server, self.topic)
        headers = {"Accept": "application/json"}
        ah = self._auth_header()
        if ah:
            headers["Authorization"] = ah
        try:
            resp = requests.get(url, headers=headers, stream=True)
            try:
                resp.raw.settimeout(0.1)
            except:
                pass
            self._resp = resp
        except Exception as e:
            # try again soon
            self._resp = None

    def send(self, text):
        url = self.server + "/" + self.topic
        headers = {"User-Agent": "esp32-mpy-ntfy", "Accept": "application/json"}
        ah = self._auth_header()
        if ah:
            headers["Authorization"] = ah
        try:
            requests.post(url, data=text, headers=headers)
        except:
            # ignore transient errors; sending is best-effort
            pass

    def poll_message(self):
        """
        Non-blocking.
        Returns one message tuple (msg_id, text, ts) if available, else None.
        """
        if self._resp is None:
            self._open_stream()
            return
        try:
            line = self._resp.raw.readline()
        except OSError as e:
            # Timeout -> brief pause; reconnect only on real errors
            if hasattr(e, "errno") and e.errno not in (errno.ETIMEDOUT, errno.EAGAIN):
                try:
                    self._resp.close()
                except:
                    pass
                time.sleep(0.5)
                self._open_stream()
            return
        except Exception:
            try:
                self._resp.close()
            except:
                pass
            time.sleep(0.5)
            self._open_stream()
            return

        if not line:
            # EOF -> reconnect
            try:
                self._resp.close()
            except:
                pass
            time.sleep(0.5)
            self._open_stream()
            return

        # One JSON event per line
        try:
            evt = json.loads(line)
        except Exception:
            return

        if evt and evt.get("event") == "message":
            return (evt.get("id") or "", evt.get("message") or "", evt.get("time") or 0)

        return None
