from Config import AntConfig
from RoboControl.Robot.Component.Sensor.Vcnl4000 import Vcnl4000Set




class LegSensorsVcnl4000(Vcnl4000Set):
    def __init__(self, protocol):
        AntConfig.FRONT_LEFT_LEG_VCNL4020["protocol"] = protocol
        AntConfig.FRONT_RIGHT_LEG_VCNL4020["protocol"] = protocol
        AntConfig.CENTER_LEFT_LEG_VCNL4020["protocol"] = protocol
        AntConfig.CENTER_RIGHT_LEG_VCNL4020["protocol"] = protocol
        AntConfig.BACK_LEFT_LEG_VCNL4020["protocol"] = protocol
        AntConfig.BACK_RIGHT_LEG_VCNL4020["protocol"] = protocol

        sensor_list = [
            AntConfig.FRONT_LEFT_LEG_VCNL4020,
            AntConfig.FRONT_RIGHT_LEG_VCNL4020,
            AntConfig.CENTER_LEFT_LEG_VCNL4020,
            AntConfig.CENTER_RIGHT_LEG_VCNL4020,
            AntConfig.BACK_LEFT_LEG_VCNL4020,
            AntConfig.BACK_RIGHT_LEG_VCNL4020
        ]

        super().__init__(sensor_list, protocol)
