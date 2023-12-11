""" A program to make LEDs light up, flash and display sequences"""

from machine import Pin
import time

# define output pins
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

counter = 1 # set the counter to start at 1

while counter < 11:
    print("Counter at: " + str(counter))
    red.value(1)
    amber.value(0)
    green.value(0)
    
    time.sleep(0.5)
    
    red.value(0)
    amber.value(1)
    green.value(0)
    
    time.sleep(0.5)
    
    red.value(0)
    amber.value(0)
    green.value(1)
    
    time.sleep(0.5)
    
    counter += 1

red.value(0)
amber.value(0)
green.value(0)
