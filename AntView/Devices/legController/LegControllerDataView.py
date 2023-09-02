import customtkinter as ctk

from Devices.AntDeviceConfig import AntDeviceConfig
from Devices.LegController.LegController import LegController
from RoboControl.Robot.AbstractRobot.AbstractRobot import AbstractRobot
from RoboControl.Robot.Component.Actor.servo.ServoSet import ServoSet
from RoboControl.Robot.Component.generic.currentSensor.CurrentSensorSet import CurrentSensorSet
from RoboView.Robot.Device.Viewer.DeviceView import DeviceView
from RoboView.Robot.Viewer.WindowBar import WindowBar
from RoboView.Robot.component.sensor.generic.currentSensor.CurrentSensorDataView import CurrentSensorDataView
from RoboView.Robot.component.actor.servo.view.ServoDataView import ServoDataView


class LegControllersDataView(DeviceView):  # AntLegControllerDataView extends MotionControllerDataView
    FRAME_NAME: str = "Leg Controller Data"

    def __init__(self, root: ctk.CTkFrame, device: LegController, window_bar: WindowBar):
        super().__init__(root, device, window_bar)
        self.make_display(device)

    def add_currents(self, currents: CurrentSensorSet) -> None:
        for current in currents:
            view = CurrentSensorDataView.create_view(self._display, current, self._settings_key)
            # self.add_component(view)

    def add_servos(self, servos: ServoSet) -> None:
        for servo in servos:
            view = ServoDataView(self._display, servo, self._settings_key)
            # self.add_component(view)

    def set_robot(self, asai: AbstractRobot) -> bool:
        return self.set_robot_with_device(asai, AntDeviceConfig.LEG_CONTROLLER, LegController.__name__)

    def make_display_legacy(self, robot_name: str, motion_controller: LegController) -> None:
        self.set_device(robot_name, motion_controller)
        self.add_servos(motion_controller.get_servo_set())
        self.add_currents(motion_controller.get_current_sensors())

    def make_display(self, device):
        self.add_servos(device.get_servo_set())
        self.add_currents(device.get_current_sensors())

        # for sensor in vcln_4000_sensors:
        # view = DistanceSensorDataView.create_view(self._display , sensor.get_distance_sensor())
        # if view is not None:
        # view._frame.place(x = 50, y = 50 ,width = 50, height = 50)

        # view = LuxSensorDataView.create_view(self._display , sensor.get_lux_sensor())
        # view._frame.place(x = 150, y = 50 ,width = 50, height = 50)
