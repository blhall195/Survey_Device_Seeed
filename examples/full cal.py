# Write your code here :-)
# SPDX-License-Identifier: Unlicense
# SPDX-License-Identifier: Unlicense
"""
This example uses I2C mode and no interrupt pin. It uses single measurement mode,
so each retrieval of `rm.magnetic` takes ``rm.measurement_time`` to complete
"""

import board
import rm3100
from seeed_xiao_nrf52840 import IMU, Battery
import time
import array
import gc
import math

from mag_cal.calibration import Calibration
from mag_cal.utils import read_fixture

import displayio
import terminalio
from adafruit_display_text import bitmap_label as label
from adafruit_displayio_sh1107 import SH1107, DISPLAY_OFFSET_ADAFRUIT_128x128_OLED_5297
from adafruit_bitmap_font import bitmap_font

font = bitmap_font.load_font("lib/fonts/terminal.bdf")

displayio.release_displays()

# For I2C
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d)

# For SPI:
# import busio
# spi_bus = busio.SPI(board.SCK, board.MOSI)
# display_bus = displayio.FourWire(spi_bus, command=board.D6, chip_select=board.D5, reset=board.D9)

# Width, height and rotation for Monochrome 1.12" 128x128 OLED
WIDTH = 128
HEIGHT = 128
ROTATION = 90

# Border width
BORDER = 2

display = SH1107(
    display_bus,
    width=WIDTH,
    height=HEIGHT,
    display_offset=DISPLAY_OFFSET_ADAFRUIT_128x128_OLED_5297,
    rotation=ROTATION,
)

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
white = displayio.Palette(1)
white[0] = 0xFFFFFF  # White
black = displayio.Palette(1)
black[0] = 0x000000  # Black


FONTSCALE = 2



i2c = board.I2C()
rm = rm3100.RM3100_I2C(i2c, i2c_address=0x20)

grav_array = []
mag_array =[]

print("perfoming general")
print("calibration")

for i in range(24):
    mag = rm.magnetic
    mag_list = list(mag)
    mag_list[0], mag_list[1], mag_list[2] = mag_list[1], mag_list[0], mag_list[2]
    mag = tuple(mag_list)
    mag_array.append(mag)

    with IMU() as imu:
        grav = imu.acceleration
        grav_list = list(grav)
        grav_list[0], grav_list[1], grav_list[2] = grav_list[1], grav_list[0], grav_list[2]
        grav = tuple(grav_list)
    grav_array.append(grav)
    print(i)

calib = Calibration()
cal_fit_ellipsoid = calib.fit_ellipsoid(mag_array, grav_array)



print("perfoming laser alignment")
mag_grav_pairs = []
grav_array = []
mag_array =[]

for i in range(4):
    mag = rm.magnetic
    mag_list = list(mag)
    mag_list[0], mag_list[1], mag_list[2] = mag_list[1], mag_list[0], mag_list[2]
    mag = tuple(mag_list)
    mag_array.append(mag)

    with IMU() as imu:
        grav = imu.acceleration
        grav_list = list(grav)
        grav_list[0], grav_list[1], grav_list[2] = grav_list[1], grav_list[0], grav_list[2]
        grav = tuple(grav_list)
    grav_array.append(grav)
    print(i)

mag_grav_pairs = list(zip(mag_array, grav_array))
#print(mag_grav_pairs)
#cal_fit_to_axis = calib.fit_to_axis(mag_grav_pairs, axis='Y')



print("perfoming non-linear fit")
mag_grav_pairs = []
grav_array = []
mag_array =[]

for i in range(4):
    mag = rm.magnetic
    mag_list = list(mag)
    mag_list[0], mag_list[1], mag_list[2] = mag_list[1], mag_list[0], mag_list[2]
    mag = tuple(mag_list)
    mag_array.append(mag)

    with IMU() as imu:
        grav = imu.acceleration
        grav_list = list(grav)
        grav_list[0], grav_list[1], grav_list[2] = grav_list[1], grav_list[0], grav_list[2]
        grav = tuple(grav_list)
    grav_array.append(grav)
    print(i)
mag_grav_pairs = list(zip(mag_array, grav_array))
#print(mag_grav_pairs)
#cal_fit_non_linear = calib.fit_non_linear(mag_grav_pairs, axis='Y',param_count=5)


while True:

    with Battery() as bat:
        Battery_voltage = bat.voltage
    bat_percentage = (Battery_voltage/4.3)*32
    bat_percentage = int(bat_percentage)

    mag = rm.magnetic
    micro_teslas = rm.convert_to_microteslas(mag)
    mag_list = list(mag)
    mag_list[0], mag_list[1], mag_list[2] = mag_list[1], mag_list[0], mag_list[2]
    mag = tuple(mag_list)

    with IMU() as imu:
        grav = imu.acceleration
        grav_list = list(grav)
        grav_list[0], grav_list[1], grav_list[2] = grav_list[1], grav_list[0], grav_list[2]
        grav = tuple(grav_list)

    azimuth, inclination, roll = calib.get_angles(mag, grav)
    print(f"{azimuth:05.1f}° {inclination:+05.1f}°")
    print(micro_teslas)#

    s= "1.13m"
    a = label.Label(font, text=s, color=0xFFFFFF,x=0,y=44,scale=FONTSCALE)
    b = azimuth
    b = str(b)
    b = f"{b}°"
    b = label.Label(font, text=b, color=0xFFFFFF,x=0,y=78,scale=FONTSCALE)
    c = inclination
    c = str(c)
    c = f"{c}°"
    c = label.Label(font, text=c, color=0xFFFFFF,x=0,y=112,scale=FONTSCALE)

    #code for displaying battery
    small_bitmap_1 = displayio.Bitmap(32, 15, 1)
    small_square_1 = displayio.TileGrid(small_bitmap_1, pixel_shader=white, x=90, y=0)
    small_bitmap_2 = displayio.Bitmap(30, 13, 1)
    small_square_2 = displayio.TileGrid(small_bitmap_2, pixel_shader=black, x=91, y=1)
    small_bitmap_3 = displayio.Bitmap(3, 6, 1)
    small_square_3 = displayio.TileGrid(small_bitmap_3, pixel_shader=white, x=122, y=4)
    small_bitmap_4 = displayio.Bitmap(bat_percentage, 13, 1)
    small_square_4 = displayio.TileGrid(small_bitmap_4, pixel_shader=white, x=91, y=1)
    #battery_percentage = bat_percentage
    #battery_percentage = str(battery_percentage)
    #battery_percentage = f"{battery_percentage}%"
    #battery_percentage = label.Label(font, text=battery_percentage, color=0xFFFFFF,x=50,y=6,scale=2)

    splash = displayio.Group()
    display.show(splash)
    splash.append(a)
    splash.append(c)
    splash.append(b)
    splash.append(small_square_1)
    splash.append(small_square_2)
    splash.append(small_square_3)
    splash.append(small_square_4)
    #splash.append(battery_percentage)






