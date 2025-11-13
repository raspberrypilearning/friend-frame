## Connect to WiFi

--- task ---

Create a new file called `config.py` and save it to the microcontroller.

--- /task ---

--- task ---

Set the variables:

```python
WIFI_SSID   = "YourWiFi"
WIFI_PASS   = "YourPassword"
NTFY_SERVER = "https://ntfy.sh"
NTFY_TOPIC  = "your-topic"       # The topic you created earlier
DEVICE_ID   = "frame-a"          # use "frame-b" on a second device etc.
NTFY_TOKEN  = None
```

--- /task ---

--- task ---

Save `config.py`.

--- /task ---

--- task ---

Open `main.py`.

--- /task ---

--- task ---

Import the config variables.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 3
---
from machine import Pin, PWM
import time
from config import WIFI_SSID, WIFI_PASS, NTFY_SERVER, NTFY_TOPIC, NTFY_TOKEN

r = machine.PWM(Pin(15), freq=1000)
g = machine.PWM(Pin(13), freq=1000)
b = machine.PWM(Pin(12), freq=1000)

--- /code ---

--- /task ---

--- task ---

Import network, json and requests.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 4-6
---
from machine import Pin, PWM
import time
from config import WIFI_SSID, WIFI_PASS, NTFY_SERVER, NTFY_TOPIC, NTFY_TOKEN
import network
import ujson as json
import urequests as requests

r = machine.PWM(Pin(15), freq=1000)
g = machine.PWM(Pin(13), freq=1000)
b = machine.PWM(Pin(12), freq=1000)

--- /code ---

--- /task ---

--- task ---

Add a function to connect to WiFi and flash blue when connected.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 18-30
---
def set_rgb(rval, gval, bval):
    r.duty(int((rval/255)*1023))
    g.duty(int((gval/255)*1023))
    b.duty(int((bval/255)*1023))


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


set_rgb(255, 0, 0)  # red

--- /code ---

--- /task ---

--- task ---

**Delete** this section of code that you created in the last step.

--- code ---
---
language: python
line_numbers: true
line_number_start: 33
line_highlights: 33-39
---
set_rgb(255, 0, 0)  # red
time.sleep(1)
set_rgb(0, 255, 0)  # green
time.sleep(1)
set_rgb(0, 0, 255)
time.sleep(1)
set_rgb(0, 0, 0)

--- /code ---

--- /task ---

--- task ---

Call the WiFi connect function. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 18
line_highlights: 33
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


wifi_connect()

--- /code ---

--- /task ---

--- task ---

**Test** Run your code. You should see the RGB LED flash blue when it has connected to WiFi.

--- /task ---