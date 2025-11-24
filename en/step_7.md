## Check topic

--- task ---

Add your **unique** topic name as a variable.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 5
---
from helper import LED, WiFi

WIFI_SSID = "your_ssid"
WIFI_PASS = "your_pass"
TOPIC = "your-topic"

led = LED(r=15, g=13, b=12)

def connected():
    led.blink("blue")


WiFi.connect(WIFI_SSID, WIFI_PASS, on_success=connected)

--- /code ---

--- /task ---

--- task ---

Import the ntfy helper.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 1
---
from helper import LED, WiFi, Ntfy

--- /code ---

--- /task ---

--- task ---

Import the time library.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 2
---
from helper import LED, WiFi, Ntfy
import time

--- /code ---

--- /task ---

--- task ---

Add code to keep checking ntfy for notifications posted to your topic.

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 15-19
---
def connected():
    led.blink("blue")


WiFi.connect(WIFI_SSID, WIFI_PASS, on_success=connected)
ntfy = Ntfy(topic=TOPIC)

while True:
    message = ntfy.poll_message()
    time.sleep(0.05)

--- /code ---

--- /task --- 

--- task ---

Turn green when a notification from your topic is found.

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 19-20
---
def connected():
    led.blink("blue")


WiFi.connect(WIFI_SSID, WIFI_PASS, on_success=connected)
ntfy = Ntfy(topic=TOPIC)

while True:
    message = ntfy.poll_message()
    if message:
        led.on("green")
    time.sleep(0.05)

--- /code ---

--- /task ---

--- task ---

**Test**: 
- Save and run the code.
Your RGB LED should flash blue when connected to WiFi.

- Post a message to your topic.
Your RGB LED should turn green when a new notification is received.

--- /task ---

--- task ---

Press the Stop/restart backend button to stop the code.
![Red stop button](images/stop.png){:width="60px"}

--- /task ---
