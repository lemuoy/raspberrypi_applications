import RPi.GPIO as GPIO
import time

# The four variables bellow indicates the number of GPIO pin thats connected to the hardware components
led1 = 17
led2 = 27
led3 = 22
button = 26

# The gpio.BCM command allows each GPIO pin's connection to be identified by numbers from 1 to 27
gpio.setmode(gpio.BCM)

gpio.setup(led1, gpio.OUT)
gpio.setup(led2, gpio.OUT)
gpio.setup(led3, gpio.OUT)

gpio.setup(button, gpio.IN)

# All leds must be powered off at the begining of the program 
gpio.output(led1, gpio.LOW)
gpio.output(led2, gpio.LOW)
gpio.output(led3, gpio.LOW)

# This variable assigns the button's state before the while loop starts  
previous_button_state = gpio.input(button)
# The led index assigns what led is ready to be used in each time
led_index = 0

while true:
    time.sleep(0.01) # This command has the function of spare CPU use, running in 100Hz 
    button_state = gpio.input(button)
    if button_state != previous_button_state:
        previous_button_state = button_state
        if button_state == gpio.HIGH:
            if led_index == 0:
                gpio.output(led1, gpio.HIGH)
                gpio.output(led2, gpio.LOW)
                gpio.output(led3, gpio.LOW)
                led_index = 1
            elif led_index == 1:
                gpio.output(led1, gpio.LOW)
                gpio.output(led2, gpio.HIGH)
                gpio.output(led3, gpio.LOW)
                led_index = 2
            else: 
                gpio.output(led1, gpio.LOW)
                gpio.output(led2, gpio.LOW)
                gpio.output(led3, gpio.HIGH)
                led_index = 0


gpio.cleanup()