# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
"""
Based on example by Mark Roberts (mdroberts1243).

This example writes text to the display, and draws a series of squares and a rectangle.
"""

import board
import busio
import displayio
import terminalio
from adafruit_display_text import bitmap_label as label
from adafruit_displayio_sh1107 import SH1107, DISPLAY_OFFSET_ADAFRUIT_128x128_OLED_5297
from adafruit_bitmap_font import bitmap_font

font = bitmap_font.load_font("lib/fonts/terminal.bdf")

import random

displayio.release_displays()
i2c=busio.I2C(board.SCL,board.SDA,frequency=400000)
#i2c = board.I2C(frequency=400000)  # uses board.SCL and board.SDA
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
while True:
    distance = random.uniform(0.0, 30)
    distance = round(distance, 2)
    distance = f"{distance}m"
    distance = label.Label(font, text=distance, color=0xFFFFFF,x=0,y=44,scale=FONTSCALE)

    compass = random.uniform(0.0, 259)
    compass = round(compass, 2)
    compass = str(compass)
    compass = f"{compass}°"
    compass = label.Label(font, text=compass, color=0xFFFFFF,x=0,y=78,scale=FONTSCALE)

    clino = random.uniform(-90.0, 90.0)
    clino = round(clino, 2)
    clino = str(clino)
    clino = f"{clino}°"
    clino = label.Label(font, text=clino, color=0xFFFFFF,x=0,y=112,scale=FONTSCALE)

    Battery_amount = random.randint(0,31)

    #code for displaying battery
    small_bitmap_1 = displayio.Bitmap(32, 15, 1)
    small_square_1 = displayio.TileGrid(small_bitmap_1, pixel_shader=white, x=90, y=0)
    small_bitmap_2 = displayio.Bitmap(30, 13, 1)
    small_square_2 = displayio.TileGrid(small_bitmap_2, pixel_shader=black, x=91, y=1)
    small_bitmap_3 = displayio.Bitmap(3, 6, 1)
    small_square_3 = displayio.TileGrid(small_bitmap_3, pixel_shader=white, x=122, y=4)
    small_bitmap_4 = displayio.Bitmap(Battery_amount, 13, 1)
    small_square_4 = displayio.TileGrid(small_bitmap_4, pixel_shader=white, x=91, y=1)


    #update display
    splash = displayio.Group()
    splash.append(distance)
    splash.append(compass)
    splash.append(clino)
    splash.append(small_square_1)
    splash.append(small_square_2)
    splash.append(small_square_3)
    splash.append(small_square_4)
    display.show(splash)

