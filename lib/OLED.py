#to run call OLED.Update(distance,compass,clino,battery_percentage)

import board
import busio
import digitalio
import displayio

from i2c import i2c
from adafruit_display_text import bitmap_label as label
from adafruit_bitmap_font import bitmap_font
from adafruit_displayio_sh1107 import SH1107, DISPLAY_OFFSET_ADAFRUIT_128x128_OLED_5297

#initalise displays
displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d)

# Width, height and rotation for Monochrome 1.12" 128x128 OLED
WIDTH = 128
HEIGHT = 128
ROTATION = 90

display = SH1107(
    display_bus,
    width=WIDTH,
    height=HEIGHT,
    display_offset=DISPLAY_OFFSET_ADAFRUIT_128x128_OLED_5297,
    rotation=ROTATION,
)

font = bitmap_font.load_font("lib/fonts/terminal.bdf")
color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
white = displayio.Palette(1)
white[0] = 0xFFFFFF  # White
black = displayio.Palette(1)
black[0] = 0x000000  # Black

FONTSCALE = 3

def update(distance,compass,clino,battery_percentage):

    distance = label.Label(font, text=distance, color=0xFFFFFF,x=0,y=36,scale=FONTSCALE)

    compass = round(compass, 2)
    compass = f"{compass}°"
    compass = label.Label(font, text=compass, color=0xFFFFFF,x=0,y=72,scale=FONTSCALE)

    clino = round(clino, 2)
    clino = f"{clino}°"
    clino = label.Label(font, text=clino, color=0xFFFFFF,x=0,y=106,scale=FONTSCALE)

    #code for displaying battery
    battery_amount = int((battery_percentage/100)*32)
    small_bitmap_1 = displayio.Bitmap(32, 15, 1)
    small_square_1 = displayio.TileGrid(small_bitmap_1, pixel_shader=white, x=90, y=0)
    small_bitmap_2 = displayio.Bitmap(30, 13, 1)
    small_square_2 = displayio.TileGrid(small_bitmap_2, pixel_shader=black, x=91, y=1)
    small_bitmap_3 = displayio.Bitmap(3, 6, 1)
    small_square_3 = displayio.TileGrid(small_bitmap_3, pixel_shader=white, x=122, y=4)
    small_bitmap_4 = displayio.Bitmap(battery_amount, 13, 1)
    small_square_4 = displayio.TileGrid(small_bitmap_4, pixel_shader=white, x=91, y=1)

    Blutooth = label.Label(font, text="BLE Connected", color=0xFFFFFF,x=0,y=6,scale=1)

    #update display
    splash = displayio.Group()
    splash.append(distance)
    splash.append(compass)
    splash.append(clino)
    splash.append(small_square_1)
    splash.append(small_square_2)
    splash.append(small_square_3)
    splash.append(small_square_4)
    splash.append(Blutooth)
    display.show(splash)

