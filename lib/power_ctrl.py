import board
import digitalio
#initalise power pins
en_pin = digitalio.DigitalInOut(board.D1)
en_pin.direction = digitalio.Direction.OUTPUT

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

def power_on():
    en_pin.value = True
    led.value = False

def power_off():
    en_pin.value =False
    led.value = True


