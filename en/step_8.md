## Respond to specific messages

Only respond to notifications from another frame ("rajib").

--- task ---

Add device name variables. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 7-8
---
from helper import LED, WiFi, Ntfy
import time

WIFI_SSID = "alice_ssid"
WIFI_PASS = "alice_pass"
TOPIC = "your-topic"
MY_DEVICE = "alice"       # Use "rajib" on your friend's frame
FRIEND_DEVICE = "rajib"   # Use "alice" on your friend's frame

led = LED(r=15, g=13, b=12)

--- /code ---

--- /task ---

### Respond only to notifications from a friend

--- task ---

Check the message for specific text.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 22-24
---
def connected():
    led.blink("blue")


WiFi.connect(WIFI_SSID, WIFI_PASS, on_success=connected)
ntfy = Ntfy(topic=TOPIC)

while True:
    message = ntfy.poll_message()
    if message:
        message_text = message[1]
        if message_text == FRIEND_DEVICE:
            led.on("green")
    time.sleep(0.05)

--- /code ---

--- /task ---

--- task ---

**Test**: 
- Save and run the code.
Your RGB LED should blink blue when connected to WiFi.

- Post a specific message ("rajib") to your topic.
Your RGB LED should turn green.

- Post a different message (e.g. "hello") to your topic.
Your RGB LED should **not** turn on.

--- /task ---

--- task ---

Press the Stop/restart backend button to stop the code.
![Red stop button](images/stop.png){:width="60px"}

--- /task ---