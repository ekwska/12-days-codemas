from machine import Pin, PWM
import time

buzzer = PWM(Pin(13))

buzzer.freq(1000)  # sets the tone
buzzer.duty_u16(10000) # sets the volume

time.sleep(1)

buzzer.duty_u16(0)