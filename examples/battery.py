# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 Phil Underwood for Underwood Underground
#
# SPDX-License-Identifier: Unlicense
import board

from seeed_xiao_nrf52840 import Battery

with Battery() as bat:
    print(f"Charge complete: {bat.charge_status}")
    print(f"Voltage: {bat.voltage}")
    print(f"Charge_current high?: {bat.charge_current}")
    print("Setting charge current to high")
    bat.charge_current = bat.CHARGE_100MA
    print(f"Charge_current high?: {bat.charge_current}")
