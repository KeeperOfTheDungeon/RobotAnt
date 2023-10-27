from Config import AntComponents
from RoboControl.Robot.Component.Sensor.Vcnl4000 import Vcnl4000Set


class HeadSensorsVcnl4020Set(Vcnl4000Set):
    def __init__(self, protocol):
        AntComponents.HEAD_VCNL_4000_LEFT_SIDE["protocol"] = protocol
        AntComponents.HEAD_VCNL_4000_LEFT["protocol"] = protocol
        AntComponents.HEAD_VCNL_4000_CENTER["protocol"] = protocol
        AntComponents.HEAD_VCNL_4000_RIGHT["protocol"] = protocol
        AntComponents.HEAD_VCNL_4000_RIGHT_SIDE["protocol"] = protocol

        sensor_list = [
            AntComponents.HEAD_VCNL_4000_LEFT_SIDE,
            AntComponents.HEAD_VCNL_4000_LEFT,
            AntComponents.HEAD_VCNL_4000_CENTER,
            AntComponents.HEAD_VCNL_4000_RIGHT,
            AntComponents.HEAD_VCNL_4000_RIGHT_SIDE
        ]

        super().__init__(sensor_list, protocol)
