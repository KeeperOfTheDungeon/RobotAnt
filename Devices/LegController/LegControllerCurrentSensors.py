from Config import AntConfig
from RoboControl.Robot.Component.Sensor.CurrentSensor import CurrentSensorSet


class LegControllerCurrentSensors(CurrentSensorSet):
    def __init__(self, protocol):
        AntConfig.LEFT_SERVO_CURRENT["protocol"] = protocol
        AntConfig.CENTER_SERVO_CURRENT["protocol"] = protocol
        AntConfig.RIGHT_SERVO_CURRENT["protocol"] = protocol

        sensor_list = [
            AntConfig.LEFT_SERVO_CURRENT,
            AntConfig.CENTER_SERVO_CURRENT,
            AntConfig.RIGHT_SERVO_CURRENT
        ]

        super().__init__(sensor_list, protocol)
