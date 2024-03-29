from Devices.LegSensors.LegSensorsDataAquisator import LegSensorsDataAquisator
from Devices.LegSensors.LegSensorsLedSet import LegSensorsLedSet
from Devices.LegSensors.LegSensorsLightSensorSet import LegSensorsLightSensorSet
from Devices.LegSensors.LegSensorsProtocol import LegSensorsProtocol
from Devices.LegSensors.LegSensorsVcnl4000 import LegSensorsVcnl4000
from RoboControl.Robot.Component.Actor.Led import Led
from RoboControl.Robot.Device.RobotDevice import RobotDevice


class LegSensors(RobotDevice):
    _vcnl_4000_set: LegSensorsVcnl4000  # TODO should be 4020

    def build(self):
        self._protocol = LegSensorsProtocol(self)

        self._aquisators = LegSensorsDataAquisator.get_data_aquisators()

        self._led_set = LegSensorsLedSet(self._protocol.get_led_protocol())
        self.add_component_set(self._led_set)

        self._light_sensor_set = LegSensorsLightSensorSet(self._protocol.get_light_sensors_protocol())
        self.add_component_set(self._light_sensor_set)


        self._vcnl_4000_set = LegSensorsVcnl4000(self._protocol.get_vcnl4000_protocol())
        self.add_component_set(self._vcnl_4000_set)

        self.build_protocol()



    def build_protocol(self):
        super().build_protocol()

        self.add_command_processor_list(self._led_set.get_command_processors())
        self.add_command_processor_list(self._vcnl_4000_set.get_command_processors())

        self.add_message_processor_list(self._led_set.get_message_processors())
        self.add_message_processor_list(self._vcnl_4000_set.get_message_processors())

        self.add_stream_processor_list(self._led_set.get_stream_processors())
        self.add_stream_processor_list(self._vcnl_4000_set.get_stream_processors())

    def get_led_set(self):
        return self._led_set

    def get_vcnl_4000_set(self):
        return self._vcnl_4000_set

    def load_setup(self):
        self._vcnl_4000_set.load_settings()
