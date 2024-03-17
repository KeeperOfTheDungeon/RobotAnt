from Config import AntConfig
from RoboControl.Robot.Component.Sensor.TMF882x import TMF882xSet


class HeadSensorsTMF882xSet(TMF882xSet):

    def __init__(self, protocol):
        AntConfig.HeadSensors.FRONT_TMF882x_SENSOR["protocol"] = protocol

        super().__init__(
            AntConfig.HeadSensors.sensor_list,
            protocol
        )
