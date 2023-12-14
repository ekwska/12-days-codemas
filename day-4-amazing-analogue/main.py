from machine import ADC, Pin
import time

def setup_led(pin_number):
    return Pin(pin_number, Pin.OUT)

potentiometer = ADC(Pin(27))
green = setup_led(18)

my_delay = 0

while True:
    my_delay = potentiometer.read_u16() / 65000
 
    green.value(1)
    time.sleep(my_delay)
    
    green.value(0)
    time.sleep(my_delay)