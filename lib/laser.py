import board
import busio
import digitalio
import gc

from laser_egismos import Laser, LaserCommandFailedError

def initialize_uart():
    global uart
    uart = busio.UART(board.TX, board.RX, baudrate=9600)
    return uart

uart = initialize_uart()

laser_power = digitalio.DigitalInOut(board.D3)
laser_power.switch_to_output(True)

laser = Laser(uart)

def laser_on():
    try:
        laser.laser_on()
    except Exception:
        uart.reset_input_buffer()
        print("Laser on failed")
        return "Laser on failed"

def laser_off():
    try:
        laser.laser_off()
    except Exception:
        uart.reset_input_buffer()
        print("Laser off failed")
        return "Laser off failed"

def buzzer_on():
    try:
        laser.buzzer_on()
    except Exception:
        uart.reset_input_buffer()
        print("Buzzer on failed")
        return "Buzzer on failed"

def buzzer_off():
    try:
        laser.buzzer_off()
    except Exception:
        uart.reset_input_buffer()
        print("Buzzer off failed")
        return "Buzzer off failed"

def take_measurment():
    try:
        distance = laser.distance
        distance = distance/100
        distance = round(distance,2)
        distance = f"{distance}m"
        return(distance)
    except Exception as e:
        print(e)
        uart.reset_input_buffer()
        return "Measurement Failed"



