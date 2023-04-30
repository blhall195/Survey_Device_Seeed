# Write your code here :-)
import board
import digitalio
import time

# Connect the EN pin of the power supply to a GPIO pin on the microcontroller
en_pin = digitalio.DigitalInOut(board.D1)
en_pin.direction = digitalio.Direction.OUTPUT
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
laser_en_pin = digitalio.DigitalInOut(board.D3)
laser_en_pin.direction = digitalio.Direction.OUTPUT

while True:
    # Turn on the power supply by pulling the EN pin high
    #en_pin.value = True
    #led.value = False
    #laser_en_pin.value = True
    time.sleep(1)

    en_pin.value = False
    led.value = True
    #laser_en_pin.value = True

    time.sleep(100)
    #en_pin.value = True
    #led.value = False
    #laser_en_pin.value = True
