#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# # Initialize the color sensor.
line_sensor = ColorSensor(Port.S3)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Calculate the light thresholds. Choose values based on your measurements.
BLACK = 7
WHITE = 88

# Calculate the average mid point.
MID_POINT= (BLACK + WHITE) / 2

DRIVE_SPEED = 60
KP = 1.5 

while line_sensor.reflection() > 10:
        robot.drive(DRIVE_SPEED, 0)

# Start following the line endlessly.
while True:

    DEVIATION =  MID_POINT - line_sensor.reflection()

    TURN_RATE = KP * DEVIATION 

    # Set the drive base speed and turn rate.
    robot.drive(DRIVE_SPEED, TURN_RATE)

    if(line_sensor.reflection() == 0):
        robot.stop()

    wait(10)

