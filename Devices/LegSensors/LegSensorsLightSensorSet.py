from Config import AntConfig
from RoboControl.Robot.Component.Sensor.LightSensor import LightSensorSet




class LegSensorsLightSensorSet(LightSensorSet):

    def __init__(self, protocol):
        AntConfig.LEFT_LIGHT_SENSOR["protocol"] = protocol
        AntConfig.CENTER_LIGHT_SENSOR["protocol"] = protocol
        AntConfig.RIGHT_LIGHT_SENSOR["protocol"] = protocol

        sensor_list = [
            AntConfig.LEFT_LIGHT_SENSOR,
            AntConfig.CENTER_LIGHT_SENSOR,
            AntConfig.RIGHT_LIGHT_SENSOR,
        ]

        super().__init__(sensor_list, protocol)


