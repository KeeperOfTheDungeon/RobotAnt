import customtkinter as ctk

from Devices.AntDeviceConfig import AntDeviceConfig
from Devices.HeadSensors.HeadSensors import HeadSensors
from RoboControl.Robot.AbstractRobot.AbstractRobot import AbstractRobot
from RoboView.Robot.Viewer.WindowBar import WindowBar

from RoboView.Robot.Device.Viewer.DeviceView import DeviceView
from RoboView.Robot.component.sensor.generic.distance.view.DistanceSensorDataView import DistanceSensorDataView
from RoboView.Robot.component.sensor.generic.lux.view.LuxSensorDataView import LuxSensorDataView


class HeadSensorsDataView(DeviceView):
    FRAME_NAME: str = "Head Sensors Data"

    def __init__(self, root: ctk.CTkFrame, device: HeadSensors, window_bar: WindowBar):
        super().__init__(root, device, window_bar)
        self.make_display(device)

    def make_display(self, device):
        vcln_4000_sensors = device.get_vcnl_4000_set()

        for sensor in vcln_4000_sensors:
            view = DistanceSensorDataView.create_view(
                self._display, sensor.get_distance_sensor(), self._settings_key)

            view = LuxSensorDataView.create_view(
                self._display, sensor.get_lux_sensor(), self._settings_key)

    def make_display_legacy(self, robot_name: str, head_sensors: HeadSensors) -> None:
        self.set_device(robot_name, head_sensors)

        for sensor in head_sensors.get_mlx90614_set():
            view = TemperatureSensorDataView.create_view(self._display, sensor.get_ambient_sensor(), self._settings_key)
            self.add_component(view)
            view = TemperatureSensorDataView.create_view(self._display, sensor.get_object_sensor(), self._settings_key)
            self.add_component(view)

        for sensor in head_sensors.get_vcnl_4000_set():
            view = LuxSensorDataView.create_view(self._display, sensor.get_lux_sensor(), self._settings_key)
            self.add_component(view)
            view = DistanceSensorDataView.create_view(self._display, sensor.get_distance_sensor(), self._settings_key)
            self.add_component(view)

        for sensor in head_sensors.get_bmp085_set():
            view = TemperatureSensorDataView.create_view(
                self._display, sensor.get_temperature_sensor(), self._settings_key
            )
            self.add_component(view)
            view = BarometricSensorDataView.create_view(
                self._display, sensor.get_barometric_sensor(), self._settings_key
            )
            self.add_component(view)

    def set_robot(self, robot: AbstractRobot) -> bool:
        return self.set_robot_with_device(robot, AntDeviceConfig.HEAD_SENSORS, HeadSensors.__name__)

    """ TODO
    def add_detector(self, detector: DigitalDetector) -> ComponentView:
        if detector is None:
            return MissingComponentView(DigitalDetector.__name__)
        return DetectorValueView(detector.get_value(), False)
    """
