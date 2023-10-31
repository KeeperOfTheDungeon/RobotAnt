from tkinter import messagebox

import customtkinter as ctk

from Devices.AntDeviceConfig import AntDeviceConfig
from Devices.LegController.LegController import LegController
from RoboControl.Robot.AbstractRobot.AbstractRobot import AbstractRobot

from RoboControl.Robot.Component.Sensor.CurrentSensor import CurrentSensorSet
from RoboView.Robot.Device.Viewer.DeviceView import DeviceView
from RoboView.Robot.component.sensor.generic.currentSensor.CurrentSensorDataView import CurrentSensorDataView
from RoboView.Robot.component.actor.servo.view.ServoDataView import ServoDataView


class LegControllersDataView(DeviceView):  # AntLegControllerDataView extends MotionControllerDataView
    FRAME_NAME: str = "Leg Controller Data"
    _device: LegController

    def make_display(self, robot_name: str, motion_controller: LegController):
        self.set_device(robot_name, motion_controller)
        x_cursor, y_cursor = 20, 20
        for servo in motion_controller.get_servo_set():
            view = ServoDataView.create_view(self._display, servo, self._settings_key)
            self.add_component(view, x_cursor, y_cursor)
            view_width, view_height = view.get_frame().winfo_reqwidth(), view.get_frame().winfo_reqheight()
            x_cursor += view_width + 10
        x_cursor, y_cursor = 20, 170
        for current in motion_controller.get_current_sensors():
            view = CurrentSensorDataView.create_view(self._display, current, self._settings_key)
            self.add_component(view, x_cursor, y_cursor)
            view_width, view_height = view.get_frame().winfo_reqwidth(), view.get_frame().winfo_reqheight()
            x_cursor += view_width + 10

    def set_robot(self, robot: AbstractRobot) -> bool:
        sensors: LegController = robot.get_device_on_name(AntDeviceConfig.LEG_CONTROLLER["DeviceName"])
        if sensors is None:
            messagebox.showerror("Error", "No leg controllers available!")
            return False
        self.make_display(robot.get_name(), sensors)
        return True
