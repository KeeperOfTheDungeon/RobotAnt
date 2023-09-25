from Config.AntComponents import AntComponents, MOTION_CONTROLLER
from Devices.LegController.LegControllerCurrentSensors import LegControllerCurrentSensors
from Devices.LegController.LegControllerDataAquisator import LegControllerDataAquisator
from Devices.LegController.LegControllerProtocol import LegControllerProtocol
from Devices.LegController.LegControllerServoSet import LegControllerServoSet
from RoboControl.Robot.Device.RobotDevice import RobotDevice

from RoboControl.Robot.Device.RobotDevice import RobotDevice


class LegController(RobotDevice):
    _current_sensor_set: LegControllerCurrentSensors
    _servo_set: LegControllerServoSet
    _temperature_sensor_set: "LegControllerLm75"
    _motion_controller: "AntMotionController"

    def build(self):
        self._aquisators = LegControllerDataAquisator.get_data_aquisators()

        self._protocol = LegControllerProtocol(self)

        self._servo_set = LegControllerServoSet(self._protocol.get_servo_protocol())
        self.add_components(self._servo_set)

        self._current_sensor_set = LegControllerCurrentSensors(self._protocol.get_current_protocol())
        self.add_components(self._current_sensor_set)

        # self._temperature_sensor_set = LegControllerLm75(self._protocol.get_temperature_protocol())
        # self.add_components(self._temperature_sensor_set)

        # self._motion_controller = AntMotionController(MOTION_CONTROLLER, LegControllerProtocol.get_motion_protocol(), self)
        # self.add_components(self._motion_controller)

        self.build_protocol()

    def build_protocol(self):
        super().build_protocol()
        for hw_set in [self._servo_set, self._current_sensor_set]:
            self._remote_command_processor_list.extend(hw_set.get_command_processors())
            self._remote_message_processor_list.extend(hw_set.get_message_processors())
            self._remote_stream_processor_list.extend(hw_set.get_stream_processors())

    def get_servo_set(self) -> LegControllerServoSet:
        return self._servo_set

    def get_current_sensors(self) -> LegControllerCurrentSensors:
        return self._current_sensor_set

    def get_temperature_sensors(self) -> "LegControllerLm75":
        raise ValueError("WIP LegControllerLm75")
        return self._temperature_sensor_set

    def load_setup(self):
        for servo in self._servo_set:
            servo.remote_loadDefaults()
            servo.remote_get_settings()
            servo.remote_get_servo_speed()
            servo.remote_get_servo_status()

        for current in self._current_sensor_set:
            current.remote_getSettings()

        for lm75 in self._temperature_sensor_set:
            lm75.remote_getSettings()
