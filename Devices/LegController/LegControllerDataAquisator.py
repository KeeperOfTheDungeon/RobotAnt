from RoboControl.Robot.Device.control.DataAquisator import DataAquisator
from RoboControl.Robot.Device.control.DeviceAquisators import DeviceAquisators

AQUISATE_SERVOS_POSITIONS = 3
AQUISATE_SERVOS_DESTINATIONS = 4
AQUISATE_SERVOS_STATUS = 5
AQUISATE_CURRENT_VALUES = 6
AQUISATE_CURRENT_CONSUMPTIONS = 7
AQUISATE_CURRENT_MAX = 8


class LegControllerDataAquisator(DeviceAquisators):
    @classmethod
    def get_data_aquisators(cls):
        return super().get_data_aquisators() + [
            DataAquisator("servos positions", 10, AQUISATE_SERVOS_POSITIONS),
            DataAquisator("servos destinationss", 10, AQUISATE_SERVOS_DESTINATIONS),
            DataAquisator("servos status", 10, AQUISATE_SERVOS_STATUS),
            DataAquisator("current values", 10, AQUISATE_CURRENT_VALUES),
            DataAquisator("current consumptions", 10, AQUISATE_CURRENT_CONSUMPTIONS),
            DataAquisator("current mex", 10, AQUISATE_CURRENT_MAX),
        ]
