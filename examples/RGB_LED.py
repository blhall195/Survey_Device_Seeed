import board
import digitalio
import time

LED_Green = digitalio.DigitalInOut(board.LED_GREEN)
LED_Green.switch_to_output()
LED_Red = digitalio.DigitalInOut(board.LED_RED)
LED_Red.switch_to_output()
LED_Blue = digitalio.DigitalInOut(board.LED_BLUE)
LED_Blue.switch_to_output()

while True:
    LED_Green.value = True
    time.sleep(1)
    LED_Green.value = False
    time.sleep(1)
    LED_Green.value = True
    time.sleep(1)
    LED_Red.value = True
    time.sleep(1)
    LED_Red.value = False
    time.sleep(1)
    LED_Blue.value = True
    time.sleep(1)
    LED_Blue.value = True
    time.sleep(1)
    LED_Blue.value = False
    time.sleep(1)
    LED_Blue.value = True
