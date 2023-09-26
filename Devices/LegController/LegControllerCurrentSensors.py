from Config import AntComponents
from RoboControl.Robot.Component.generic.currentSensor.CurrentSensorSet import CurrentSensorSet


class LegControllerCurrentSensors(CurrentSensorSet):
    def __init__(self, protocol):
        AntComponents.LEFT_SERVO_CURRENT["protocol"] = protocol
        AntComponents.CENTER_SERVO_CURRENT["protocol"] = protocol
        AntComponents.RIGHT_SERVO_CURRENT["protocol"] = protocol

        sensor_list = [
            AntComponents.LEFT_SERVO_CURRENT,
            AntComponents.CENTER_SERVO_CURRENT,
            AntComponents.RIGHT_SERVO_CURRENT
        ]

        super().__init__(sensor_list, protocol)
