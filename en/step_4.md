## RGB LED

An RGB LED has four legs.

![RGB LED with the longer leg labelled GND. The leg on the left is the Red leg, the leg on the right is the Blue leg and the leg second from the right is the Green leg.](images/rgb-led-legs.png)

--- task ---

Add the RGB LED to the breadboard in **column E**, so that each leg sits in its own row.

The second leg from the top should be the longest leg.

![RGB LED placed in breadboard](images/RGB-bb-7.png)

--- /task ---

--- task ---

Connect a the GND pin on your microcontroller to the same row as that GND leg of the RGB LED.

![GND pin from ESP board connected to the same row as the RGB GND leg.](images/RGB-bb-6.png)

--- /task ---

--- task ---

Add a resistor to **column B**. 

In our example, it connects the Red leg on row 24 to row 20.

![Resistor added to the breadboard.](images/RGB-bb-5.png)

--- /task ---

--- task ---

Add another resistor to **column C**. 

In our example, it connects the Green leg on row 26 to row 22.

![Second resistor added to the breadboard.](images/RGB-bb-4.png)

--- /task ---

--- task ---

Add a resistor to **column D**. 

In our example, it connects the Blue leg on row 27 to row 23.

![Third resistor added to the breadboard.](images/RGB-bb-3.png)

--- /task ---

--- task ---

Use jumper cables to connect the resistors to the microcontroller pins. 

- 'Red' resistor    >>> Pin D5 (GPIO 15)
- 'Green' resistor  >>> Pin D6 (GPIO 13)
- 'Blue' resistor   >>> Pin D7 (GPIO 12)

![Cables connecting the resistors to the microcontroller pins.](images/RGB-bb.png)

--- /task ---

--- task ---

Connect the microcontroller to your computer using a usb cable.

--- /task ---

# Control the RGB LED with code 

--- task ---

Click in the main editor pane of Thonny. 

Enter this code. 

``` python
from machine import Pin, PWM
import time

r = machine.PWM(Pin(15), freq=1000)
g = machine.PWM(Pin(13), freq=1000)
b = machine.PWM(Pin(12), freq=1000)

def set_rgb(rval, gval, bval):
    r.duty(int((rval/255)*1023))
    g.duty(int((gval/255)*1023))
    b.duty(int((bval/255)*1023))


set_rgb(255, 0, 0)  # red
time.sleep(1)
set_rgb(0, 255, 0)  # green
time.sleep(1)
set_rgb(0, 0, 255)  # blue
time.sleep(1)
set_rgb(0, 0, 0)    # off
```

--- /task ---

--- task ---

Click the Green **Run** button and the RGB LED will show red, green and blue for one second each, then turn off.

--- /task ---

--- task ---

Click the **Stop** button.  

--- /task ---

### Save your program to your microcontroller

--- task ---

Make sure you have Stopped the program, then click the 'Save' icon, or choose 'Save' from the 'File' menu.

--- /task ---

Thonny will give you the option to save the file on **This computer**, or the **MicroPython device**. 

![Option buttons to save the file on **This computer** or the **MicroPython device**](images/save-on-device.png){:width="300px"}

--- task ---

Choose **MicroPython device**.

Enter `main.py` as the file name and Click 'OK'. 

**Tip:** You need to enter the `.py` file extension so that Thonny recognises the file as a Python file. 

--- /task ---

**Debug**: If you get an error saying the device is busy, you need to first 'Stop' the program running on the Pico.


- Check ntfy
- LED change colour if ntfy
- 
- 