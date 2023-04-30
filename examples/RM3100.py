# SPDX-License-Identifier: Unlicense
"""
This example uses I2C mode and no interrupt pin. It uses single measurement mode,
so each retrieval of `rm.magnetic` takes ``rm.measurement_time`` to complete
"""

import board
import rm3100
import time

i2c = board.I2C()
rm = rm3100.RM3100_I2C(i2c, i2c_address=0x20)

while True:
    print(rm.magnetic)
    time.sleep(1)
