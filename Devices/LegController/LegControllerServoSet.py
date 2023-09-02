from Config import AntComponents
from RoboControl.Robot.Component.Actor.servo.ServoSet import ServoSet


class LegControllerServos(ServoSet):
    def __init__(self, protocol):
        AntComponents.LEG_CONTROLLER_LEFT_SERVO["protocol"] = protocol
        AntComponents.LEG_CONTROLLER_CENTER_SERVO["protocol"] = protocol
        AntComponents.LEG_CONTROLLER_RIGHT_SERVO["protocol"] = protocol
        AntComponents.LEG_CONTROLLER_HEAD_SERVO["protocol"] = protocol

        sensor_list = [
            AntComponents.LEG_CONTROLLER_LEFT_SERVO,
            AntComponents.LEG_CONTROLLER_CENTER_SERVO,
            AntComponents.LEG_CONTROLLER_RIGHT_SERVO,
            AntComponents.LEG_CONTROLLER_HEAD_SERVO
        ]

        super().__init__(sensor_list, protocol)
