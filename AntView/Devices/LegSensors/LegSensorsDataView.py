from tkinter import messagebox

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
    _device: LegSensors

    def make_display(self, robot_name: str, sensors: LegSensors) -> None:
        self.set_device(robot_name, sensors)
        x_cursor, y_cursor = 20, 20
        for sensor in sensors.get_vcnl_4000_set():
            lux_view = LuxSensorDataView.create_view(self._display, sensor.get_lux_sensor(), self._settings_key)
            view_width, view_height = lux_view.get_frame().winfo_reqwidth(), lux_view.get_frame().winfo_reqheight()
            self.add_component(lux_view, x_cursor, y_cursor)
            distance_view = DistanceSensorDataView.create_view(
                self._display, sensor.get_distance_sensor(), self._settings_key
            )
            self.add_component(distance_view, x_cursor, y_cursor + 90)
            x_cursor += view_width
        for led in sensors.get_led_set():
            # led_view = LedDataView.create_view(self._display, led, self._settings_key)
            pass

    def set_robot(self, robot: AbstractRobot) -> bool:
        sensors: LegSensors = robot.get_device_on_name(AntDeviceConfig.LEG_SENSORS.get_name())
        if sensors is None:
            messagebox.showerror("Error", "No leg sensors available!")
            return False
        self.make_display(robot.get_name(), sensors)
        return True

    # TODO
    # def add_detector(self, detector: DigitalDetector) -> ComponentView:
    #     if detector is None:
    #         return MissingComponentView(DigitalDetector.__name__)
    #     return DetectorValueView(detector.get_value(), False)

