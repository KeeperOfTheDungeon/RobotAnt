from time import sleep

from Config.AntConfig import AntDeviceConfig
from Devices.HeadSensors.HeadSensors import HeadSensors
from Devices.LegController.LegController import LegController
from RoboControl.Com.Connection import Connection
from RoboControl.Com.SerialConnection import SerialConnection
from Devices.LegSensors.LegSensors import LegSensors
from RoboControl.Robot.Device.Generic.DataHub.DataHub import DataHub
from RoboControl.Robot.Device.RobotDevice import RobotDevice
from RoboControl.Robot.Robot import Robot


class Ant(Robot):
    def __init__(self):
        super().__init__("ant")
        self.add_devices()
        self._connection: Connection = SerialConnection()

    def run(self):
        while True:
            self._data_hub.remote_ping_device()
            sleep(1)

    def connect(self, connection: SerialConnection) -> None:
        self._connection = connection
        super().connect(connection)
        

    def add_device(self, device: RobotDevice) -> None:
        self._device_list.append(device)
        device.set_transmitter(self._connection)

    def add_devices(self):
        self._data_hub = DataHub(AntDeviceConfig.MAIN_DATA_HUB)
        self.add_device(self._data_hub)

        self._head_sensors = HeadSensors(AntDeviceConfig.HEAD_SENSORS)
        self.add_device(self._head_sensors)

        self._leg_sensors = LegSensors(AntDeviceConfig.LEG_SENSORS)
        self.add_device(self._leg_sensors)

        self._leg_controller = LegController(AntDeviceConfig.LEG_CONTROLLER)
        self.add_device(self._leg_controller)

        # self._tail_board = TailBoard(AntDeviceConfig.TAIL_BOARD)
        # self.add_device(self._tail_board)

        # self._ir_com = IrCom(AntDeviceConfig.IR_COM)
        # self.add_device(self._ir_com)

        # self._pixy_controller = PixyController(AntDeviceConfig.PIXY_CONTROLLER)
        # self.add_device(self._pixy_controller)

        # self._behavior = AntBehavior(self)
        # self.add_device(self._behavior)

    def get_head_sensors(self):
        return self._head_sensors

    def get_leg_sensors(self):
        return self._leg_sensors

    def get_leg_controller(self):
        return self._leg_controller

    def get_data_hub(self):
        return self._data_hub
