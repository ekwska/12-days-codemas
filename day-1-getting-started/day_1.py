from machine import Pin

print("This is my Pico talking!")

# Set Pin 25 as an output pin
onboard_led = Pin(25, Pin.OUT)
light = 0
str_light = "off" if light == 0 else "on"

# Send voltage to the pin onboard to turn it on
onboard_led.value(light)
print("My Pico's light is: " + str_light)
