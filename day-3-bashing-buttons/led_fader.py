from machine import ADC, Pin, PWM
import time

potentiometer = ADC(Pin(27))
led = PWM(Pin(18))

# sets how often to switch the power between on and off for the LED
led.freq(1000)

reading = 0

while True:
    reading = potentiometer.read_u16()
    print("Potentiometer reads: " + str(reading))
    
    led.duty_u16(reading)
    time.sleep(0.001)