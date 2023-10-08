from tkinter import messagebox

import customtkinter as ctk

from Devices.AntDeviceConfig import AntDeviceConfig
from Devices.LegController.LegController import LegController
from RoboControl.Robot.AbstractRobot.AbstractRobot import AbstractRobot
from RoboControl.Robot.Component.Actor.servo.ServoSet import ServoSet
from RoboView.Robot.Device.Viewer.DeviceView import DeviceView
from RoboView.Robot.Viewer.WindowBar import WindowBar
from RoboView.Robot.component.actor.servo.view.ServoControlView import ServoControlView


class LegControllersControlView(DeviceView):  # AntLegControllerControlView extends MotionControllerControlView
    FRAME_NAME: str = "Leg Controller Control"
    _device: LegController

    def make_display(self, robot_name: str, motion_controller: LegController):
        self.set_device(robot_name, motion_controller)
        x_cursor, y_cursor = 20, 20
        for servo in motion_controller.get_servo_set():
            view = ServoControlView.create_view(self._display, servo, self._settings_key)
            self.add_component(view, x_cursor, y_cursor)
            view_width, view_height = view.get_frame().winfo_reqwidth() - 20, view.get_frame().winfo_reqheight()
            x_cursor += view_width

    def set_robot(self, robot: AbstractRobot) -> bool:
        sensors: LegController = robot.get_device_on_name(AntDeviceConfig.LEG_CONTROLLER.get_name())
        if sensors is None:
            messagebox.showerror("Error", "No leg controllers available!")
            return False
        self.make_display(robot.get_name(), sensors)
        return True
