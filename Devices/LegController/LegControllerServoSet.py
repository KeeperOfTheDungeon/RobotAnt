
from Config import AntConfig
from RoboControl.Robot.Component.Actor.Servo import ServoSet



class LegControllerServoSet(ServoSet):
    def __init__(self, protocol):

        AntConfig.LEG_CONTROLLER_LEFT_SERVO["protocol"] = protocol
        AntConfig.LEG_CONTROLLER_CENTER_SERVO["protocol"] = protocol
        AntConfig.LEG_CONTROLLER_RIGHT_SERVO["protocol"] = protocol
        AntConfig.LEG_CONTROLLER_HEAD_SERVO["protocol"] = protocol

        sensor_list = [
            AntConfig.LEG_CONTROLLER_LEFT_SERVO,
            AntConfig.LEG_CONTROLLER_CENTER_SERVO,
            AntConfig.LEG_CONTROLLER_RIGHT_SERVO,
            AntConfig.LEG_CONTROLLER_HEAD_SERVO
        ]

        super().__init__(sensor_list, protocol)
