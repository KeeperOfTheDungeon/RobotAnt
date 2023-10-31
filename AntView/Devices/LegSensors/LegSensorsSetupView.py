from tkinter import messagebox

from Devices.AntDeviceConfig import AntDeviceConfig
from Devices.LegSensors.LegSensors import LegSensors
from RoboControl.Robot.AbstractRobot.AbstractRobot import AbstractRobot
from RoboView.Robot.Device.Viewer.DeviceView import DeviceView
from RoboView.Robot.component.actor.led.view.LedControlView import LedControlView


class LegSensorsSetupView(DeviceView):
    FRAME_NAME: str = "Leg Sensors Setup"

    def make_display(self, robot_name: str, leg_sensors: LegSensors):
        self.set_device(robot_name, leg_sensors)
        x_cursor, y_cursor = 50, 50
        for led in leg_sensors.get_led_set():
            view = LedControlView.create_view(self._display, led, self._settings_key)
            self.add_component(view, x_cursor, y_cursor)
            view_width, view_height = view.get_frame().winfo_reqwidth(), view.get_frame().winfo_reqheight()
            x_cursor += view_width - 20

        # x_cursor, y_cursor = 50, 150
        # for led in leg_sensors.get_vcnl_4000_set():
        #     view = Vcnl4000SetupView.create_view(self._display, led, self._settings_key)
        #     self.add_component(view, x_cursor, y_cursor)
        #     view_width, view_height = view.get_frame().winfo_reqwidth(), view.get_frame().winfo_reqheight()
        #     x_cursor += view_width - 20

    def set_robot(self, robot: AbstractRobot) -> bool:
        sensors: LegSensors = robot.get_device_on_name(AntDeviceConfig.LEG_SENSORS["DeviceName"])
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
