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

    def __init__(self, root: ctk.CTkFrame, device: LegController, window_bar: WindowBar):
        super().__init__(root, device, window_bar)
        self.make_display(device)

    def make_display(self, device):
        servos = device.get_servo_set()
        for servo in servos:
            view = ServoControlView.create_view(self._display, servo, self._settings_key)

    def set_robot(self, robot: AbstractRobot) -> bool:
        return self.set_robot_with_device(robot, AntDeviceConfig.LEG_CONTROLLER, LegController.__name__)

    def make_display_legacy(self, robot_name: str, motion_controller: LegController) -> None:
        self.set_device(robot_name, motion_controller)
        self.add_servos(motion_controller.get_servo_set())

    def add_servos(self, servos: ServoSet) -> None:
        for servo in servos:
            view = ServoControlView(self._display, servo, self._settings_key)
            self.add_component(view)
