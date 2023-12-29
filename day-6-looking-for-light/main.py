from machine import ADC, Pin, PWM
import time


# define the pins for the LEDs
def setup_led(pin_number):
    return Pin(pin_number, Pin.OUT)

def play_buzzer_beep(buzzer, volume):
     # also play a tone on the buzzer
    buzzer.duty_u16(volume)
    time.sleep(1)
    buzzer.duty_u16(0)

# set up our LED names and GPIO pin numbers
red = setup_led(20)
amber = setup_led(19)
green = setup_led(18)

# define the pin for the light sensor
lightsensor = ADC(Pin(26))

# set up the buzzer
buzzer = PWM(Pin(13))
buzzer.freq(1000)  # sets the tone
volume = 10000

while True:
    # read the sensor value
    light = lightsensor.read_u16()
    lightpercent = round(light / 65535 * 100, 1)

    print("Light value : ", str(light))
    print("Percentage of light: ", str(lightpercent) + "%")
    
    time.sleep(1)
    
    if lightpercent <= 30:
        red.value(1)
        amber.value(0)
        green.value(0)

    elif 30 < lightpercent < 60:
        red.value(0)
        amber.value(1)
        green.value(0)
        
    elif lightpercent >= 60:
        red.value(0)
        amber.value(0)
        green.value(1)
        
        # also play a beep every second the light is green
        play_buzzer_beep(buzzer, volume)