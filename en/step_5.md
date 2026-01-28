## Connect to WiFi

--- task ---

Import the WiFi class.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 1
---
from helper import LED, WiFi

led = LED(r=15, g=13, b=12)

led.blink()

--- /code ---

--- /task ---

--- task ---

Set the variables. 

Make sure you enter your WiFi SSID and password.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 3-4
---
from helper import LED, WiFi

WIFI_SSID = "alice_ssid"
WIFI_PASS = "alice_pass"

led = LED(r=15, g=13, b=12)

led.blink()

--- /code ---

--- /task ---

--- task ---

**Delete** this section of code that you created in the last step.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 8
---
led.blink()

--- /code ---

--- /task ---

--- task ---

Add a function to blink blue when connected.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 8-9
---
from helper import LED, WiFi

WIFI_SSID = "alice_ssid"
WIFI_PASS = "alice_pass"

led = LED(r=15, g=13, b=12)

def connected():
    led.blink("blue")

--- /code ---

--- /task ---

--- task ---

Call the 'connected' function when the device connects to WiFi. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 12
---
from helper import LED, WiFi

WIFI_SSID = "alice_ssid"
WIFI_PASS = "alice_pass"

led = LED(r=15, g=13, b=12)

def connected():
    led.blink("blue")


WiFi.connect(WIFI_SSID, WIFI_PASS, on_success=connected)

--- /code ---

--- /task ---

--- task ---

**Test** Save and run your code. You should see the RGB LED blink blue when it has connected to WiFi.

--- /task ---
