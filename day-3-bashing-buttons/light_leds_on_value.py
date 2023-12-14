from machine import ADC, Pin
import time

def setup_led(pin_number):
    return Pin(pin_number, Pin.OUT)

potentiometer = ADC(Pin(27))
green = setup_led(18)
amber = setup_led(19)
red = setup_led(20)

green.value(0)
amber.value(0)
red.value(0)

reading = 0

while True:
    reading = potentiometer.read_u16()
    print("Potentiometer reads: " + str(reading))
    time.sleep(0.1)
    
    if reading <= 20000:
        red.value(1)
        amber.value(0)
        green.value(0)
    elif 20000 < reading < 40000:
        red.value(0)
        amber.value(1)
        green.value(0)
    elif reading >= 40000:
        red.value(0)
        amber.value(0)
        green.value(1)