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
WIFI_SSID = "your_ssid"  # Your friend's SSID
WIFI_PASS = "your_pass"  # Your friend's password
MY_DEVICE = "frame-b"
FRIEND_DEVICE = "frame-a"
--- /code ---

--- /task ---

--- task ---

Save the code to the second MicroPython device.

--- /task ---

--- task ---

**Your frame**:
- Place your first build behind or inside a photo frame of your friend so you can see the LED.

**Your friend's frame**:
- Place your second build behind or inside a photo frame of you. 
- Give it to your friend.

--- /task ---

--- task ---

**Test**: 
- Power up both devices.
The RGB LEDs should blink blue when connected to WiFi.

- Post the message ("frame-b") to your topic.
Your RGB LED should turn green.

- Post the message ("frame-a") to your topic.
Your **friend's** RGB LED should turn green.

--- /task ---
