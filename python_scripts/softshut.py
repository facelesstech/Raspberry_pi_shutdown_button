#import the modules to send commands to the system and access GPIO pins
from subprocess import call
import RPi.GPIO as gpio
import os

# Define a function to keep script running
def loop():
    raw_input()

# Define a function to run when an interrupt is called
def shutdown(pin):
    gpio.setup(16, gpio.OUT) # Set up pin 16 as an output
    gpio.output(16, True) # Turn on pin 16 (LED)
    os.system("sudo shutdown -h now") # Shutdown command

gpio.setmode(gpio.BOARD) # Set pin numbering to board numbering
gpio.setup(15, gpio.IN) # Set up pin 15 as an input
gpio.add_event_detect(15, gpio.RISING, callback=shutdown, bouncetime=200) #Set up an interrupt to look for button presses
 
loop() # Run the loop function to keep script running
