from machine import Pin, PWM
import time

buzzer = PWM(Pin(13))

buzzer.duty_u16(10000)
buzzer.freq(1000)
time.sleep(1)

buzzer.freq(500)
time.sleep(1)

buzzer.duty_u16(0)