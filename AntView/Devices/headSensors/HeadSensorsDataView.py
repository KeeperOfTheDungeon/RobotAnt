from tkinter import messagebox

from Config.AntConfig import AntDeviceConfig
from Devices.HeadSensors.HeadSensors import HeadSensors
from RoboControl.Robot.AbstractRobot.AbstractRobot import AbstractRobot

from RoboView.Robot.Device.Viewer.DeviceView import DeviceView
from RoboView.Robot.component.sensor.generic.distance.view.DistanceSensorDataView import DistanceSensorDataView
from RoboView.Robot.component.sensor.generic.lux.view.LuxSensorDataView import LuxSensorDataView


class HeadSensorsDataView(DeviceView):
    FRAME_NAME: str = "Head Sensors Data"
    _device: HeadSensors

    def make_display(self, robot_name: str, head_sensors: HeadSensors):
        self.set_device(robot_name, head_sensors)

        # TODO
        # for sensor in head_sensors.getMlx90614Set():
        #     view = TemperatureSensorDataView.create_view(self._display, sensor.get_ambient_sensor(), self._settings_key)
        #     view = TemperatureSensorDataView.create_view(self._display, sensor.get_object_sensor(), self._settings_key)

        x_cursor, y_cursor = 20, 20
        for (sensor) in head_sensors.get_tmf8821_set():
            #view = LuxSensorDataView.create_view(self._display, sensor.get_lux_sensor(), self._settings_key)
            #self.add_component(view, x_cursor, y_cursor)
            for s in sensor.get_distance_sensors():
                view = DistanceSensorDataView.create_view(self._display, s, self._settings_key)
                self.add_component(view, x_cursor, y_cursor + 90)
                view_width, view_height = view.get_frame().winfo_reqwidth(), view.get_frame().winfo_reqheight()
                x_cursor += view_width + 10

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
