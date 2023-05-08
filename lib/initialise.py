import board
import busio
import digitalio
import displayio



#initalise displays
displayio.release_displays()
i2c=busio.I2C(board.SCL,board.SDA,frequency=400000)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d)


