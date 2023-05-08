import power_ctrl
power_ctrl.power_on()
import OLED
import mag_sensor
import laser
import seeed
import time
import calibration as calib

calib.calibrate()

while True:

    distance = laser.take_measurment()
    battery_percentage = seeed.battery_percentage()
    azimuth, inclination, roll = calib.true_values(mag_sensor.mag_readings(), seeed.acceleration())

    print(distance)
    print(azimuth)
    print(inclination)
    print(battery_percentage)
    OLED.update(distance,azimuth,inclination,battery_percentage)
    time.sleep(1)

    laser.laser_off()

    time.sleep(1)

    laser.laser_on()

    time.sleep(2)


