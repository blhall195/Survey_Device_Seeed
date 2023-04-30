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

i2c = board.I2C()
rm = rm3100.RM3100_I2C(i2c, i2c_address=0x20)

grav = []
mag =[]
mem = gc.mem_free()
print(mem)
gc.collect()
mem = gc.mem_free()
print(mem)

while True:
    read_mag = rm.magnetic
    mag_array = array.array('f', read_mag)
    print("Magnetometer: ",mag_array)

    with IMU() as imu:
        read_grav = imu.acceleration
    grav_array = array.array('f', read_grav)
    print("Acceleration: ",grav_array)

    time.sleep(1)



