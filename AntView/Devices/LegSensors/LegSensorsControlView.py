import customtkinter as ctk

from Devices.AntDeviceConfig import AntDeviceConfig
from Devices.LegSensors.LegSensors import LegSensors
from RoboControl.Robot.AbstractRobot.AbstractRobot import AbstractRobot
from RoboView.Robot.Device.Viewer.DeviceView import DeviceView
from RoboView.Robot.Viewer.WindowBar import WindowBar
from RoboView.Robot.component.actor.led.view.LedControlView import LedControlView


class LegSensorsControlView(DeviceView):
    FRAME_NAME: str = "Leg Sensors Control"

    def __init__(self, root: ctk.CTkFrame, device: LegSensors, window_bar: WindowBar):
        super().__init__(root, device, window_bar)
        self.make_display(device)

    def make_display(self, device):
        leds = device.get_led_set()
        for led in leds:
            view = LedControlView.create_view(self._display, led, self._settings_key)
        # if view is not None:
        # view._frame.place(x = 50, y = 50)

    def set_robot(self, robot: AbstractRobot) -> bool:
        return self.set_robot_with_device(robot, AntDeviceConfig.LEG_SENSORS, LegSensors.__name__)

    def make_display_legacy(self, robot_name: str, leg_sensors: LegSensors) -> None:
        self.set_device(robot_name, leg_sensors)

        """
        for led in self.get_led_set():
            view = LedControlView.createView(self._display, led, self._settings_key)
            self.add_component(view)
        """

    """ TODO
    def add_detector(self, detector: DigitalDetector) -> ComponentView:
        if detector is None:
            return MissingComponentView(DigitalDetector.__name__)
        return DetectorValueView(detector.get_value(), False)
    """
