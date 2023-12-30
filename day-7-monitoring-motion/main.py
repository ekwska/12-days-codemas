from machine import Pin, PWM
import time

# define the pins for the LEDs
def setup_led(pin_number):
    return Pin(pin_number, Pin.OUT)

def setup_rgb_leds():
    # set up our LED names and GPIO pin numbers
    red = setup_led(20)
    amber = setup_led(19)
    green = setup_led(18)
    return red, amber, green

def setup_motion_sensor():
    # setup motion sensor
    pir = Pin(26, Pin.IN, Pin.PULL_DOWN)
    print("Warming up...")
    time.sleep(10)
    print("Sensor ready!")
    return pir

def alarm(buzzer, volume):
    
    buzzer.duty_u16(volume)
    
    for i in range(5):
        buzzer.freq(5000) # higher pitch
        red.value(1)
        amber.value(1)
        green.value(1)
        
        time.sleep(1)
        
        buzzer.freq(500) # lower pitch
        red.value(0)
        amber.value(0)
        green.value(0)
        
        time.sleep(1)
    
    buzzer.duty_u16(0) # turn off volume
        

# setup all leds
red, amber, green = setup_rgb_leds()
pir = setup_motion_sensor()

# set up the buzzer
buzzer = PWM(Pin(13))
buzzer.freq(1000)  # sets the tone
volume = 10000

while True:
    time.sleep(0.01) # delay to stop unnecessary program speed
    
    if pir.value() == 1:
        print("I SEE YOU!")
        
        alarm(buzzer, volume)
        
        print("Sensor active")
