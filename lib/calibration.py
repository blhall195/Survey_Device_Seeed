import mag_sensor
import seeed
import time

from mag_cal.calibration import Calibration
from mag_cal.utils import read_fixture

calib = Calibration(mag_axes="-Y+X-Z",grav_axes="-Y+X+Z")

def calibrate():

    #grav_array = []
    #mag_array =[]

    #for i in range(34):
        #mag = mag_sensor.mag_readings()
        #mag_array.append(mag)#


        #grav = seeed.acceleration()
        #grav_array.append(grav)
    #
        #print(i)
        #time.sleep(0.5)

    grav_array = [(-0.421136, -0.620937, 10.1575), (-0.0191426, -2.46221, 9.26022), (-1.72881, 7.1677, 7.30169), (-1.0995, 10.812, 0.527617), (-1.15334, -4.8658, 9.42173), (-0.642473, -9.89192, 1.57687), (-7.93699, -2.37248, -2.1344), (-9.5653, 0.437886, -3.41934), (-6.89252, -5.24028, 1.19162), (-6.88654, -3.5653, -6.49531), (0.905683, -9.06042, -0.764506), (0.295513, -9.01495, -4.00678), (-0.397208, 7.36032, -6.6341), (1.12702, 8.00518, 4.74975), (-3.31406, 2.77926, 10.6588), (-7.97767, -6.28594, 3.13699), (-3.5653, -4.32502, -7.08873), (-2.28993, -8.55673, 0.145962), (3.12502, -4.96271, 12.2297), (6.33619, -0.332602, 4.18624), (-3.21117, 10.9005, -0.504885), (-3.9984, 11.9593, -1.16411), (-7.96929, -0.580259, 11.4784), (-8.67876, -2.72901, 0.818345), (-9.34636, 2.48853, 5.28096), (1.11984, 6.2644, 8.62014), (3.44925, 3.87996, -4.1312), (5.90548, 2.28395, 4.50329), (3.4337, -8.50528, 6.12562), (0.58983, -6.49053, 5.30847), (-4.40638, -8.02193, 3.23988), (-2.73858, -3.44327, 7.78026), (0.0969093, -0.684347, 10.7318), (-0.124427, -0.232104, 10.1527)]
    mag_array = [(-5.8875, -9.4625, 35.7375), (-3.2375, -9.825, 35.775), (-1.9, -36.775, 14.5375), (1.775, -39.375, -15.8), (-2.7875, 8.525, 37.0625), (-2.1875, 42.45, 12.2625), (-35.2375, 26.725, 3.4375), (-43.4, -1.1125, -7.9125), (-38.95, 13.35, 12.6), (-31.8125, 3.45, -31.1), (-4.125, 41.2875, -18.675), (-4.2375, 30.825, -32.6875), (-5.5125, -37.425, -19.0), (-8.125, -33.375, 18.3), (-16.65, 8.775, 33.7375), (-26.2625, 25.1625, 21.5375), (-19.3125, 31.025, -27.3625), (-10.7, 43.275, 4.825), (11.5625, -0.3375, 35.3), (34.5875, -22.475, 3.05), (-22.1125, -35.75, 1.225), (-19.9125, -37.7625, -3.425), (-29.775, -6.3875, 26.1625), (-41.3125, 8.825, 5.8375), (-29.3125, -13.825, 23.1625), (26.875, -26.8, 12.2), (17.5375, -32.0875, -21.525), (28.675, -2.4375, 26.075), (-4.8125, 31.55, 26.4125), (-11.8, 32.175, 24.4), (-25.225, 30.6875, 16.5), (-22.65, 2.875, 30.525), (-0.6, -13.3, 32.8375), (-2.0125, -11.1875, 33.6875)]

    cal = calib.calibrate(mag_array, grav_array,0)

    return(cal)

def true_values(mag, grav):
    azimuth, inclination, roll = calib.get_angles(mag, grav)
    return(azimuth, inclination, roll)

