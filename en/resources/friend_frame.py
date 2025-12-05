from helper import LED, WiFi, Ntfy, Touchpad
import time

# ---- Setup ----
WIFI_SSID = "alice_ssid"
WIFI_PASS = "alice_pass"
MY_DEVICE = "alice"  # "rajib" on your friend's frame
FRIEND_DEVICE = "rajib"  # "alice" on your friend's frame
TOPIC = "your_topic"

led = LED(r=15, g=13, b=12)
clear_pad = Touchpad(5)
send_pad = Touchpad(4)


# ---- Go online ----
def connected():
    led.blink("blue")


WiFi.connect(WIFI_SSID, WIFI_PASS, on_success=connected)
ntfy = Ntfy(topic=TOPIC)

# ---- Main ----
while True:
    if clear_pad.pressed():
        led.off()

    if send_pad.pressed():
        led.blink("cyan")
        ntfy.send(MY_DEVICE)

    message = ntfy.poll_message()
    if message:
        message_text = message[1]
        if message_text == FRIEND_DEVICE:
            led.on("green")

    time.sleep(0.05)  # gentle on the CPU
