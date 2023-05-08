import board
import busio
import rm3100
from i2c import i2c

rm = rm3100.RM3100_I2C(i2c, i2c_address=0x20)

def mag_readings():
    mag = rm.magnetic
    return(mag)









