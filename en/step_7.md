## Check topic

--- task ---

Add a function to get the latest messages posted to your ntfy topic.

--- code ---
---
language: python
line_numbers: true
line_number_start: 18
line_highlights: 33-37
---
def wifi_connect():
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    if not sta.isconnected():
        sta.connect(WIFI_SSID, WIFI_PASS)
        while not sta.isconnected():
            time.sleep(0.2)
    
    set_rgb(0, 0, 255)
    time.sleep(1)
    set_rgb(0, 0, 0)

    return sta


def open_events():
    url = "{}/{}/json".format(NTFY_SERVER.rstrip("/"), NTFY_TOPIC)
    headers = {"Accept": "application/json"}
    if NTFY_TOKEN: headers["Authorization"] = NTFY_TOKEN
    return requests.get(url, headers=headers)


wifi_connect()

--- /code ---

--- /task ---

--- task ---

Complete the main program to flash green for five seconds when a message from your topic is found.

--- code ---
---
language: python
line_numbers: true
line_number_start: 33
line_highlights: 41-57
---
def open_events():
    url = "{}/{}/json".format(NTFY_SERVER.rstrip("/"), NTFY_TOPIC)
    headers = {"Accept": "application/json"}
    if NTFY_TOKEN: headers["Authorization"] = NTFY_TOKEN
    return requests.get(url, headers=headers)


wifi_connect()
set_rgb(0,0,0)  # idle: RGB LED off
resp = open_events()
while True:
    line = resp.raw.readline()
    if not line:
        resp.close()
        time.sleep(1)
        resp = open_events()
        continue
    try:
        evt = json.loads(line)
    except Exception:
        continue
    if evt.get("event") == "message":
        set_rgb(0,255,0)  # green = new message
        time.sleep(5)
        set_rgb(0,0,0)    # back to idle

--- /code ---

--- /task ---

--- task ---

**Test**: 
- Run the code 
Your RGB LED should flash blue when connected to WiFi.

- Post a message to your topic. 
Your RGB LED should turn green when a new message is received, then turn off.

--- /task ---
