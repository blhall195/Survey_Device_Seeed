from seeed_xiao_nrf52840 import IMU, Battery

def initialize_imu():
    imu = IMU()
    return imu

def initialize_Battery():
    bat = Battery()
    return bat

imu = initialize_imu()
bat = initialize_Battery()

def acceleration():
    acceleration = imu.acceleration
    return(acceleration)

def battery_percentage():
    voltage = bat.voltage
    battery_percentage = (voltage - 3.3) / (4.2 - 3.3) * 100
    return(battery_percentage)
