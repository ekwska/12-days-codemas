from machine import Pin
import time


def setup_button(pin_number):
    return Pin(pin_number, Pin.IN, Pin.PULL_DOWN)

def setup_led(pin_number):
    return Pin(pin_number, Pin.OUT)

# Set the button name and GPIO pin number
# Also set the pin as an INPUT and use a PULL DOWN
button1 = setup_button(13)
button2 = setup_button(8)
button3 = setup_button(3)

# set up our LED names and GPIO pin numbers
red = setup_led(20)
amber = setup_led(19)
green = setup_led(18)

red.value(0)
amber.value(0)
green.value(0)

while True: # loop forever
    
    time.sleep(0.2) # short delay
        
    # if both buttons are pressed    
    if button1.value() == 1:
        print("Button 1 pressed")
        red.toggle()
    elif button2.value() == 1:
        print("Button 2 pressed")
        amber.toggle()
    elif button3.value() == 1:
        print("Button 3 pressed")
        green.toggle()