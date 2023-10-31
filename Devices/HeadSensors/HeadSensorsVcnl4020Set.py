from Config import AntConfig
from RoboControl.Robot.Component.Sensor.Vcnl4000 import Vcnl4000Set


class HeadSensorsVcnl4020Set(Vcnl4000Set):
    def __init__(self, protocol):
        AntConfig.HEAD_VCNL_4000_LEFT_SIDE["protocol"] = protocol
        AntConfig.HEAD_VCNL_4000_LEFT["protocol"] = protocol
        AntConfig.HEAD_VCNL_4000_CENTER["protocol"] = protocol
        AntConfig.HEAD_VCNL_4000_RIGHT["protocol"] = protocol
        AntConfig.HEAD_VCNL_4000_RIGHT_SIDE["protocol"] = protocol

        sensor_list = [
            AntConfig.HEAD_VCNL_4000_LEFT_SIDE,
            AntConfig.HEAD_VCNL_4000_LEFT,
            AntConfig.HEAD_VCNL_4000_CENTER,
            AntConfig.HEAD_VCNL_4000_RIGHT,
            AntConfig.HEAD_VCNL_4000_RIGHT_SIDE
        ]

        super().__init__(sensor_list, protocol)
