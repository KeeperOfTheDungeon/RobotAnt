from typing import List

from Devices.HeadSensors.HeadSensorsDataAquisator import HeadSensorsDataAquisator
from Devices.HeadSensors.HeadSensorsProtocol import HeadSensorsProtocol
from Devices.HeadSensors.HeadSensorsVcnl4020Set import HeadSensorsVcnl4020Set
from RoboControl.Robot.Device.RobotDevice import RobotDevice
from RoboControl.Robot.Value.ComponentValue import ComponentValue


class HeadSensors(RobotDevice):

    def build(self):
        self._protocol = HeadSensorsProtocol(self)

        self._aquisators = HeadSensorsDataAquisator.get_data_aquisators()

        self._vcnl_4020_set = HeadSensorsVcnl4020Set(self._protocol.get_vcnl4020_protocol())
        self.add_components(self._vcnl_4020_set)
        # self._mxl90614_set = HeadMlx90614Set(self._protocol.get_mlx90614_protocol())
        # self.add_components(self._mxl90614_set)
        # self._bmp085_sensor_set = Bmp085Set(self._protocol.get_bmp085_protocol())
        # self.add_components(self._bmp085_sensor_set)
        # self._servos = AnalogServoServoSet()

        self.build_protocol()

    def build_protocol(self):
        super().build_protocol()
        self._remote_command_processor_list.extend(self._vcnl_4020_set.get_command_processors())
        self._remote_message_processor_list.extend(self._vcnl_4020_set.get_message_processors())
        self._remote_stream_processor_list.extend(self._vcnl_4020_set.get_stream_processors())

    def get_vcnl_4000_set(self):
        return self._vcnl_4020_set

    def get_mxl90614_set(self):
        raise ValueError("WIP HeadMlx90614Set")
        return self._mxl90614_set

    def get_bmp085_set(self):
        raise ValueError("WIP Bmp085Set")
        return self._bmp085_sensor_set

    def _load_setup(self):
        self._vcnl_4020_set.load_settings()
        # self._mxl90614_set.load_settings()
        # self._bmp085Sensor_set.load_settings()

    def get_servos(self) -> "AnalogServoServoSet":
        raise ValueError("WIP AnalogServoServoSet")
        return self._servos

    def get_input_values(self) -> List[ComponentValue]:
        values = []
        for sensor in self.get_mxl90614_set():
            values.append(sensor.get_ambient_value())
            values.append(sensor.get_object_value())
        values += self.get_bmp085_set().get_values()
        values += self.get_mxl90614_set().get_values()
        values += self.get_vcnl_4000_set().get_values()
        return values

    def add_bmp085_sensors(self, meta_data: "HeadSensorsMetaData") -> None:
        raise ValueError("WIP Bmp085Set")
        self._bmp085_sensor_set = Bmp085Set(
            meta_data.get_bmp085_data(),
            HeadSensorsProtocol.get_bmp085_protocol(self.get_id())
        )
        self.add_components(super().get_bmp085_set())
