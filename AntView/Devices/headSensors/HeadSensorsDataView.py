from tkinter import messagebox

from Config.AntConfig import AntDeviceConfig
from Devices.HeadSensors import HeadSensorsDataAquisator
from Devices.HeadSensors.HeadSensors import HeadSensors
from RoboControl.Robot.AbstractRobot.AbstractRobot import AbstractRobot

from RoboView.Robot.Device.Viewer.DeviceView import DeviceView
from RoboView.Robot.component.sensor.generic.distance.view.DistanceSensorDataView import DistanceSensorDataView
from RoboView.Robot.component.sensor.tmf882x.TMF882xDataView import TMF882xDataView


class HeadSensorsDataView(DeviceView):
    FRAME_NAME: str = "Head Sensors Data"
    _device: HeadSensors

    def make_display(self, robot_name: str, head_sensors: HeadSensors):
        self.set_device(robot_name, head_sensors)

        # TODO
        # for sensor in head_sensors.getMlx90614Set():
        #     view = TemperatureSensorDataView.create_view(self._display, sensor.get_ambient_sensor(), self._settings_key)
        #     view = TemperatureSensorDataView.create_view(self._display, sensor.get_object_sensor(), self._settings_key)

        TMF882xDataView(head_sensors.get_tmf8821_set(), self)

        # TODO
        # for sensor in head_sensors.get_bmp085_set():
        #    view = TemperatureSensorDataView.create_view(
        #        self._display, sensor.get_temperature_sensor(), self._settings_key
        #    )
        #    self.add_component(view)
        #    view = BarometricSensorDataView.create_view(
        #        self._display, sensor.get_barometric_sensor(), self._settings_key
        #    )
        #    self.add_component(view)

    def set_robot(self, robot: AbstractRobot) -> bool:
        sensors: HeadSensors = robot.get_device_on_name(AntDeviceConfig.HEAD_SENSORS["DeviceName"])
        if sensors is None:
            messagebox.showerror("Error", "No head sensors available!")
            return False
        self.make_display(robot.get_name(), sensors)
        return True

    # TODO
    # def add_detector(self, detector: DigitalDetector) -> ComponentView:
    #     if detector is None:
    #         return MissingComponentView(DigitalDetector.__name__)
    #     return DetectorValueView(detector.get_value(), False)
