MAIN_DATA_HUB_ID = 0

LEG_CONTROLLER_ID = 10
HEAD_SENSORS_ID = 11
TAIL_BOARD_ID = 12
LEG_SENSORS_ID = 13


class AntDeviceConfig():
    MAIN_DATA_HUB = {"DeviceId": MAIN_DATA_HUB_ID,
                     "DeviceName": "Main Data Hub"}

    HEAD_SENSORS = {"DeviceId": HEAD_SENSORS_ID,
                    "DeviceName": "head sensors"}

    LEG_CONTROLLER = {"DeviceId": LEG_CONTROLLER_ID,
                      "DeviceName": "Motion Controller"}

    LEG_SENSORS = {"DeviceId": LEG_SENSORS_ID,
                   "DeviceName": "leg sensors"}


ROBOT_NAME = {  # ROBOT_NAME(,0,DataHub.ID),
    "name": "Ant III",
    "local_id": 0,
    "global_id": 0,
}

# TMP Light Sensors


LEFT_LIGHT_SENSOR = {  # FRONT_LEFT_LEG_LED ("front left",1),
    "name": "left",
    "local_id": 0,
    "global_id": 0,
}
CENTER_LIGHT_SENSOR = {  # FRONT_LEFT_LEG_LED ("front left",1),
    "name": "center",
    "local_id": 1,
    "global_id": 0,
}

RIGHT_LIGHT_SENSOR = {  # FRONT_LEFT_LEG_LED ("front left",1),
    "name": "right",
    "local_id": 2,
    "global_id": 0,
}

# ************* LegSensorsConfiguration ******************


FRONT_LEFT_LEG_LED = {  # FRONT_LEFT_LEG_LED ("front left",1),
    "name": "front left",
    "local_id": 1,
    "global_id": 0,
}

FRONT_RIGHT_LEG_LED = {  # FRONT_RIGHT_LEG_LED ("front right",4),
    "name": "front right",
    "local_id": 4,
    "global_id": 0,
}

CENTER_LEFT_LEG_LED = {  # CENTER_LEFT_LEG_LED ("center left",0),
    "name": "center left",
    "local_id": 0,
    "global_id": 0,
}

CENTER_RIGHT_LEG_LED = {  # CENTER_RIGHT_LEG_LED ("center right",3),
    "name": "center right",
    "local_id": 3,
    "global_id": 0,
}

BACK_LEFT_LEG_LED = {  # BACK_LEFT_LEG_LED ("back left",2),
    "name": "back left",
    "local_id": 2,
    "global_id": 0,
}

BACK_RIGHT_LEG_LED = {  # BACK_RIGHT_LED ("cack right",5),
    "name": "back right",
    "local_id": 5,
    "global_id": 0,
}

# light sensors

FRONT_LEFT_LEG_VCNL4020 = {  # FRONT_LEFT_LEG_VCNL4020 ("front left",1),
    "name": "center left",
    "local_id": 1,
    "global_id": 0,
}

FRONT_RIGHT_LEG_VCNL4020 = {  # FRONT_RIGHT_LEG_4020 ("front right",4),
    "name": "front right",
    "local_id": 4,
    "global_id": 0,
}

CENTER_LEFT_LEG_VCNL4020 = {  # CENTER_LEFT_LEG_4020 ("center left",0),
    "name": "center left",
    "local_id": 0,
    "global_id": 0,
}

CENTER_RIGHT_LEG_VCNL4020 = {  # CENTER_RIGHT_LEG_VCNL4020 ("center right",3),
    "name": "center right",
    "local_id": 3,
    "global_id": 0,
}

BACK_LEFT_LEG_VCNL4020 = {  # BACK_LEFT_LEG_VCNL4020 ("back left",2),
    "name": "back left",
    "local_id": 2,
    "global_id": 0,
}

BACK_RIGHT_LEG_VCNL4020 = {  # BACK_RIGHT_LEG_VCNL4020 ("cack right",5),
    "name": "back right",
    "local_id": 5,
    "global_id": 0,
}

# ************* HeadSensorsConfiguration ******************

HEAD_SERVO = {  # HEAD_SERVO ("head servo",0),
    "name": "head servo",
    "local_id": 0,
    "global_id": 0,
}

HEAD_LEFT_MLX90614 = {  # HEAD_LEFT_MLX90614("left mlx90614",0),
    "name": "left mlx90614",
    "local_id": 0,
    "global_id": 0,
}
HEAD_RIGHT_MLX90614 = {  # HEAD_RIGHT_MLX90614("right mlx90614",1),
    "name": "right mlx90614",
    "local_id": 1,
    "global_id": 0,
}

TEMPERATURE_0 = {  # TEMPERATURE_0("t0 bmp",0),
    "name": "t1 bmp",
    "local_id": 0,
    "global_id": 0,
}
TEMPERATURE_1 = {  # TEMPERATURE_1("t1 bmp",1),
    "name": "t1 bmp",
    "local_id": 1,
    "global_id": 0,
}
TEMPERATURE_2 = {  # TEMPERATURE_2("t1 bmp",2),
    "name": "t1 bmp",
    "local_id": 2,
    "global_id": 0,
}
TEMPERATURE_3 = {  # TEMPERATURE_3("t1 bmp",3),
    "name": "t1 bmp",
    "local_id": 3,
    "global_id": 0,
}

PRESURE_0 = {  # PRESURE_0("p0",0),
    "name": "p0",
    "local_id": 0,
    "global_id": 0,
}
PRESURE_1 = {  # PRESURE_1("p1",1),
    "name": "p1",
    "local_id": 1,
    "global_id": 0,
}
PRESURE_2 = {  # PRESURE_2("p2",2),
    "name": "p2",
    "local_id": 2,
    "global_id": 0,
}
PRESURE_3 = {  # PRESURE_3("p3",3),
    "name": "p3",
    "local_id": 3,
    "global_id": 0,
}

HEAD_VCNL_4000_LEFT_SIDE = {  # HEAD_VCNL4000_LEFT_SIDE("left side",0),
    "name": "left side",
    "local_id": 0,
    "global_id": 0,
}

HEAD_VCNL_4000_LEFT = {  # HEAD_VCNL4000_LEFT("left",1),
    "name": "left",
    "local_id": 1,
    "global_id": 0,
}

HEAD_VCNL_4000_CENTER = {  # HEAD_VCNL4000_CENTER("center",2),
    "name": "center",
    "local_id": 2,
    "global_id": 0,
}
HEAD_VCNL_4000_RIGHT = {  # HEAD_VCNL4000_RIGHT("right",3),
    "name": "right",
    "local_id": 3,
    "global_id": 0,
}
HEAD_VCNL_4000_RIGHT_SIDE = {  # HEAD_VCNL4000_RIGHT_SIDE("right side",4),
    "name": "right side",
    "local_id": 4,
    "global_id": 0,
}

# ************* LegControllerConfiguration ******************

# LEFT_TEMPERATURE_SENSOR (LegControllerConfiguration.LEFT_TEMPERATURE_SENSOR),
# CENTER_TEMPERATURE_SENSOR (LegControllerConfiguration.CENTER_TEMPERATURE_SENSOR),
# RIGHT_TEMPERATURE_SENSOR (LegControllerConfiguration.RIGHT_TEMPERATURE_SENSOR),
# REGULATOR_TEMPERATURE_SENSOR (LegControllerConfiguration.REGULATOR_TEMPERATURE_SENSOR),


LEG_CONTROLLER_LEFT_SERVO = {  # LEFT_SERVO ("left",0),
    "name": "left",
    "local_id": 0,
    "global_id": 0,
}
LEG_CONTROLLER_CENTER_SERVO = {  # CENTER_SERVO ("center",1),
    "name": "center",
    "local_id": 1,
    "global_id": 0,
}
LEG_CONTROLLER_RIGHT_SERVO = {  # RIGHT_SERVO ("right",2),
    "name": "right",
    "local_id": 2,
    "global_id": 0,
}
LEG_CONTROLLER_HEAD_SERVO = {  # HEAD_SERVO ("head",3),
    "name": "head",
    "local_id": 3,
    "global_id": 0,
}

LEFT_SERVO_CURRENT = {  # LEFT_SERVO_CURRENT ("left",0),
    "name": "left",
    "local_id": 0,
    "global_id": 0,
}
CENTER_SERVO_CURRENT = {  # CENTER_SERVO_CURRENT ("center",1),
    "name": "center",
    "local_id": 1,
    "global_id": 0,
}
RIGHT_SERVO_CURRENT = {  # RIGHT_SERVO_CURRENT ("right",2),
    "name": "right",
    "local_id": 2,
    "global_id": 0,
}
# ************* TailBoardConfiguration ******************

TAIL_VCNL4020_LEFT = {  # TAIL_VCNL4020_LEFT("left vcnl4020", 0),
    "name": "left vcnl4020",
    "local_id": 0,
    "global_id": 0,
}
TAIL_VCNL4020_CENTER = {  # TAIL_VCNL4020_CENTER("center vcnl4020", 1 ),
    "name": "center vcnl4020",
    "local_id": 1,
    "global_id": 0,
}
TAIL_VCNL4020_RIGHT = {  # TAIL_VCNL4020_RIGHT("right vcnl4020", 2),
    "name": "right vcnl4020",
    "local_id": 2,
    "global_id": 0,
}

TAIL_TMP006_LEFT = {  # TAIL_TMP006_LEFT("left tmp006", 0),
    "name": "left tmp006",
    "local_id": 0,
    "global_id": 0,
}

TAIL_TMP006_CENTER = {  # TAIL_TMP006_CENTER("center tmp006", 1 ),
    "name": "center tmp006",
    "local_id": 1,
    "global_id": 0,
}

TAIL_TMP006_RIGHT = {  # TAIL_TMP006_RIGHT("right tmp006", 2),
    "name": "right tmp006",
    "local_id": 2,
    "global_id": 0,
}

ANT_MPU9150 = {  # ANT_MPU9150 ("MPU9150", 0),
    "name": "MPU9150",
    "local_id": 0,
    "global_id": 0,
}

ANT_IMU = {  # ANT_IMU ("IMU", 0),
    "name": "IMU",
    "local_id": 0,
    "global_id": 0,
}
ANT_LOCATOR = {  # ANT_LOCATOR ("locator",0 ),
    "name": "locator",
    "local_id": 0,
    "global_id": 0,
}
ANT_HEADING = {  # ANT_HEADING ("heading", 0),
    "name": "heading",
    "local_id": 0,
    "global_id": 0,
}

TAIL_LEFT_LED = {  # TAIL_LEFT_LED ("led left", 0),
    "name": "led left",
    "local_id": 0,
    "global_id": 0,
}
TAIL_RIGHT_LED = {  # TAIL_RIGHT_LED ("led right", 1),
    "name": "led right",
    "local_id": 1,
    "global_id": 0,
}


class HeadSensors:
    FRONT_TMF882x_SENSOR = {
        "name": "front",
        "local_id": 1,
        "global_id": 0,
    }

    sensor_list = [
        FRONT_TMF882x_SENSOR
    ]


class AntComponents:
    def __init__(self):
        pass


class AntComponent:
    def __init__(self, data: dict):
        self._data = data

    @property
    def local_id(self) -> int:
        return self._data["local_id"]

    @property
    def name(self) -> int:
        return self._data["name"]

    @property
    def device_id(self) -> int:
        return self._data["device_id"]

    @property
    def global_id(self) -> int:
        return self._data["global_id"]
