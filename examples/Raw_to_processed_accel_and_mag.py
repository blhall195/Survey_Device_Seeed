# Write your code here :-)
# SPDX-License-Identifier: Unlicense
# SPDX-License-Identifier: Unlicense
"""
This example uses I2C mode and no interrupt pin. It uses single measurement mode,
so each retrieval of `rm.magnetic` takes ``rm.measurement_time`` to complete
"""

import board
import rm3100
from seeed_xiao_nrf52840 import IMU
import time
import array
import gc
import math

i2c = board.I2C()
rm = rm3100.RM3100_I2C(i2c, i2c_address=0x20)

grav = []
mag =[]


def inclination_angle(acceleration):
    z, y, x = acceleration
    inclination = math.degrees(math.atan2(math.sqrt(x**2 + y**2), z))
    return -inclination if inclination < 0 else 90 - inclination

def magnetic_heading(magnetometer_data):
    # Rotate coordinate system by 90 degrees
    x, y, z = magnetometer_data[1], -magnetometer_data[0], magnetometer_data[2]

    # Compute heading in rotated coordinate system
    heading = math.atan2(y, x)
    if heading < 0:
        heading += 2*math.pi
    elif heading > 2*math.pi:
        heading -= 2*math.pi

    # Convert heading to degrees
    return math.degrees(heading)

while True:
    #read_mag = rm.magnetic

    with IMU() as imu:
        acceleration = imu.acceleration

    angle = inclination_angle(acceleration)
    time.sleep(1)

    read_mag = rm.magnetic
    magnetometer_data = array.array('f', read_mag)
    heading = magnetic_heading(magnetometer_data)
    print("Magnetic heading:", heading,", inclination:", -angle)



