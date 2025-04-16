# Created by: Jack Eddy
# Created on: April 2025
#
# This program turns a servo motor with the turning of a potentiometer

import time
import board
import pwmio
from adafruit_motor import servo
from analogio import AnalogIn

# constants
RANGE_TO_ANGLE = 180/65535

# create a PWMOut object on Pin 16.
pwm = pwmio.PWMOut(board.GP16, duty_cycle=2 ** 15, frequency=50)

potentionmeter = AnalogIn(board.GP26) # sets pot pin to pin 26/A0

# create a servo object, my_servo.
my_servo = servo.Servo(pwm, min_pulse = 650, max_pulse = 2500)

while True:
    print((potentionmeter.value))
    potentiometer_value  = potentionmeter.value

    # returns value of the potentiometer
    print(potentiometer_value )

    # changes range from 0-65535 to a corrisponding angle between 0-180
    angle = potentiometer_value * (RANGE_TO_ANGLE)
    my_servo.angle = angle
