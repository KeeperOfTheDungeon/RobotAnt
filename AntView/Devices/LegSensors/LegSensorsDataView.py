import customtkinter as ctk

from Devices.AntDeviceConfig import AntDeviceConfig
from Devices.LegSensors.LegSensors import LegSensors
from RoboControl.Robot.AbstractRobot.AbstractRobot import AbstractRobot
from RoboView.Robot.Device.Viewer.DeviceView import DeviceView
from RoboView.Robot.Viewer.WindowBar import WindowBar
from RoboView.Robot.component.sensor.generic.distance.view.DistanceSensorDataView import DistanceSensorDataView
from RoboView.Robot.component.sensor.generic.lux.view.LuxSensorDataView import LuxSensorDataView
from RoboView.Robot.component.view.ComponentView import ComponentView
from RoboView.Robot.component.view.MissingComponentView import MissingComponentView


class LegSensorsDataView(DeviceView):
    FRAME_NAME: str = "Leg Sensors Data"

    def __init__(self, root: ctk.CTkFrame, device: LegSensors, window_bar: WindowBar):
        super().__init__(root, device, window_bar)
        self.make_display("WIP", device)

    def make_display(self, robot_name: str, sensors: LegSensors) -> None:
        self.set_device(robot_name, sensors)
        for sensor in sensors.get_vcnl_4000_set():
            lux_view = LuxSensorDataView.create_view(self._display, sensor.get_lux_sensor(), self._settings_key)
            # self.add_component(lux_view)
            distance_view = DistanceSensorDataView.create_view(self._display, sensor.get_distance_sensor(),
                                                               self._settings_key)
            # self.add_component(distance_view)
        for led in sensors.get_led_set():
            # led_view = LedDataView.create_view(self._display, led, self._settings_key)
            pass

    def set_robot(self, robot: AbstractRobot) -> bool:
        return self.set_robot_with_device(robot, AntDeviceConfig.LEG_SENSORS, LegSensors.__name__)

    """ TODO
    def add_detector(self, detector: DigitalDetector) -> ComponentView:
        if detector is None:
            return MissingComponentView(DigitalDetector.__name__)
        return DetectorValueView(detector.get_value(), False)
    """
