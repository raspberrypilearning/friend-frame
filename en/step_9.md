## Build your friend's frame

--- task ---

Follow this project again to create a second build.

--- /task ---

--- task ---

Change these variables on the second build:

--- code ---
---
language: python
line_numbers: true
line_number_start: 4
---
WIFI_SSID = "rajib_ssid"  # Your friend's SSID
WIFI_PASS = "rajib_pass"  # Your friend's password
--- /code ---

**Note**: Keep your friend's WiFi password safe!

--- /task ---

--- task ---

Swap the device name variables:

--- code ---
---
language: python
line_numbers: true
line_number_start: 6
---
MY_DEVICE = "rajib"
FRIEND_DEVICE = "alice"
--- /code ---

--- /task ---

--- task ---

Save the code to the second MicroPython device.

--- /task ---

--- task ---

**Your frame**:
- Place your first build behind or inside a photo frame of your friend so you can see the LED.

![A photograph frame with a LED pulsing blue behind it.](images/friend_frame.jpeg){:width="270px"}

**Your friend's frame**:
- Place your second build behind or inside a photo frame of you. 
- Give it to your friend.

--- /task ---

--- task ---

**Test**: 
- Power up both devices.
The RGB LEDs should blink blue when connected to WiFi.

- Post the message ("rajib") to your topic.
Your RGB LED should turn green.

- Post the message ("alice") to your topic.
Your **friend's** RGB LED should turn green.

--- /task ---
