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
import busio
import digitalio
from laser_egismos import Laser, LaserCommandFailedError

import displayio
from adafruit_display_text import bitmap_label as label
from adafruit_displayio_sh1107 import SH1107, DISPLAY_OFFSET_ADAFRUIT_128x128_OLED_5297
from adafruit_bitmap_font import bitmap_font
font = bitmap_font.load_font("lib/fonts/terminal.bdf")
displayio.release_displays()
i2c=busio.I2C(board.SCL,board.SDA,frequency=400000)
#i2c = board.I2C(frequency=400000)  # uses board.SCL and board.SDA
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d)

laser_power = digitalio.DigitalInOut(board.D3)
laser_power.switch_to_output(True)

uart = busio.UART(board.D6, board.D7, baudrate=9600)

laser = Laser(uart)
laser.laser_off()

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

from mag_cal.calibration import Calibration
from mag_cal.utils import read_fixture

rm = rm3100.RM3100_I2C(i2c, i2c_address=0x20)



print("perfoming general")
print("calibration")
grav_array = []
mag_array =[]

for i in range(24):
    mag = rm.magnetic
    mag_array.append(mag)

    with IMU() as imu:
        grav = imu.acceleration
    grav_array.append(grav)

    print(i)

calib = Calibration(mag_axes="+Y+X-Z",grav_axes="-Y+X+Z")

cal = calib.calibrate(mag_array, grav_array,0)
print(cal)

mag = rm.magnetic

while True:

    with Battery() as bat:
        Battery_voltage = bat.voltage
    Battery_amount = int((Battery_voltage/4.3)*32)

    #micro_teslas = rm.convert_to_microteslas(mag)

    with IMU() as imu:
        grav = imu.acceleration
    azimuth, inclination, roll = calib.get_angles(mag, grav)
    print(f"{azimuth:05.1f}° {inclination:+05.1f}°")
    #print(micro_teslas)

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
    small_bitmap_4 = displayio.Bitmap(Battery_amount, 13, 1)
    small_square_4 = displayio.TileGrid(small_bitmap_4, pixel_shader=white, x=91, y=1)

    splash = displayio.Group()
    display.show(splash)
    splash.append(a)
    splash.append(c)
    splash.append(b)
    splash.append(small_square_1)
    splash.append(small_square_2)
    splash.append(small_square_3)
    splash.append(small_square_4)
