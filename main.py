#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the color sensor.
line_sensor = ColorSensor(Port.S3)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Calculate the light thresholds. Choose values based on your measurements.
BLACK_THRESHOLD = 7
WHITE_THRESHOLD = 78

# Calculate the average threshold.
threshold = (BLACK_THRESHOLD + WHITE_THRESHOLD) / 2

# Set the drive speed and proportional gain.
DRIVE_SPEED = 55
PROPORTIONAL_GAIN = 1

# Start following the line endlessly.
while True:
    #SoundFile("path_to_music_file.wav").play()
    # Calculate the deviation from the threshold.
    deviation = line_sensor.reflection() - threshold

    # Calculate the turn rate.
    turn_rate = PROPORTIONAL_GAIN * deviation

    # Set the drive base speed and turn rate.
    robot.drive(DRIVE_SPEED, turn_rate)

    # You can wait for a short time or do other things in this loop.
    wait(10)

    if(line_sensor.reflection() == 0):
        robot.stop()
    
