from machine import Pin, PWM, ADC
import time

potentiometer = ADC(Pin(27))
buzzer = PWM(Pin(13))

reading = 0

while True:
    time.sleep(0.01)
    reading = potentiometer.read_u16()
    buzzer.freq(500)
    buzzer.duty_u16(reading)
    print("Reading is: " + str(reading))
