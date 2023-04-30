# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Phil Underwood for Underwood Underground
#
# SPDX-License-Identifier: Unlicense
import time

import board
import busio
import digitalio

from laser_egismos import Laser, LaserCommandFailedError

laser_power = digitalio.DigitalInOut(board.D3)
laser_power.switch_to_output(True)

uart = busio.UART(board.D6, board.D7, baudrate=9600)
laser = Laser(uart)
laser.buzzer_off()

while True:
    
    time.sleep(1)
    #print(f"Distance is {laser.distance}cm")
