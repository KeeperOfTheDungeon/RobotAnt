from time import sleep
from typing import Optional

from Devices.AntDeviceConfig import AntDeviceConfig
from Devices.HeadSensors.HeadSensors import HeadSensors
from Devices.LegController.LegController import LegController
from RoboControl.Com.Connection.Connection import Connection
from RoboControl.Com.Connection.SerialConnection import SerialConnection
from Devices.LegSensors.LegSensors import LegSensors
from RoboControl.Robot.Device.Generic.DataHub.DataHub import DataHub
from RoboControl.Robot.Robot import Robot


class Ant(Robot):
    def __init__(self):
        super().__init__("ant")

        self._connection: Optional[Connection] = None
        # FIXME these aren't actually optional
        #   a better way would be to return the values from add_devices and set them here
        self._data_hub: Optional[DataHub] = None
        self._head_sensors: Optional[HeadSensors] = None
        self._leg_sensors: Optional[LegSensors] = None
        self._leg_controller: Optional[LegController] = None

    def run(self):
        while True:
            self._data_hub.remote_ping_device()
            sleep(1)

    def connect(self, connection: SerialConnection) -> None:
        self._connection = connection
        super().connect(connection)
        self.add_devices()

    def add_devices(self):
        self._data_hub = DataHub(AntDeviceConfig.MAIN_DATA_HUB)
        self._device_list.append(self._data_hub)
        self._data_hub.set_transmitter(self._connection)

        self._head_sensors = HeadSensors(AntDeviceConfig.HEAD_SENSORS)
        self._device_list.append(self._head_sensors)
        self._head_sensors.set_transmitter(self._connection)

        self._leg_sensors = LegSensors(AntDeviceConfig.LEG_SENSORS)
        self._device_list.append(self._leg_sensors)
        self._leg_sensors.set_transmitter(self._connection)

        self._leg_controller = LegController(AntDeviceConfig.LEG_CONTROLLER)
        self._device_list.append(self._leg_controller)
        self._leg_controller.set_transmitter(self._connection)

    def get_head_sensors(self):
        return self._head_sensors

    def get_leg_sensors(self):
        return self._leg_sensors

    def get_leg_controller(self):
        return self._leg_controller

    def get_data_hub(self):
        return self._data_hub


"""
#	leg = new LegController(AntDeviceId.LEG_CONTROLLER.getDeviceMetaData());    
#	this.deviceList.add(leg);
    
#	this.addMainHub(AntComponents.ROBOT_NAME.getMetaData());
    

    
    
    
    
    
#	this.deviceList.add(new HeadSensors(AntDeviceId.HEAD_SENSORS.getDeviceMetaData()));
#	this.deviceList.add(new TailBoard(AntDeviceId.TAIL_BOARD.getDeviceMetaData()));
#	this.deviceList.add(new LegSensors(AntDeviceId.LEG_SENSORS.getDeviceMetaData()));
    
#	this.deviceList.add(new IrCom(AntDeviceId.IR_COM.getDeviceMetaData()));
    
#	this.deviceList.add(new PixyController(AntDeviceId.PIXY_CONTROLLER.getDeviceMetaData()));
    
#	this.behavior = new  AntBehavior(this);
"""
