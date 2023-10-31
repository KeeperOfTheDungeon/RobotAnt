from RoboControl.Robot.AbstractRobot.DeviceConfig import DeviceConfig

MAIN_DATA_HUB_ID = 0

LEG_CONTROLLER_ID = 10
HEAD_SENSORS_ID = 11
TAIL_BOARD_ID = 12
LEG_SENSORS_ID = 13

class AntDeviceConfig(DeviceConfig):

    MAIN_DATA_HUB = {"DeviceId" : MAIN_DATA_HUB_ID,
                     "DeviceName" : "Main Data Hub"}

    HEAD_SENSORS = {"DeviceId" : HEAD_SENSORS_ID,
                     "DeviceName" : "head sensors"}

    LEG_CONTROLLER = {"DeviceId" : LEG_CONTROLLER_ID,
                     "DeviceName" : "Motion Controller"}
    
    LEG_SENSORS = {"DeviceId" : LEG_SENSORS_ID,
                     "DeviceName" : "leg sensors"}

"""
    MAIN_DATA_HUB = DeviceConfig(0, "main data hub")
    LEG_CONTROLLER = DeviceConfig(10, "leg controller")
    HEAD_SENSORS = DeviceConfig(11, "head sensors")
    TAIL_BOARD = DeviceConfig(12, "tail board")
    LEG_SENSORS = DeviceConfig(13, "leg sensors")
    IR_COM = DeviceConfig(14, "ir com")
    PIXY_CONTROLLER = DeviceConfig(42, "pixy controller")
"""