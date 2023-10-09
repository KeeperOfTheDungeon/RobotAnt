from RoboControl.Robot.Device.control.DataAquisator import DataAquisator
from RoboControl.Robot.Device.control.DeviceAquisators import DeviceAquisators

AQUISATE_SERVOS_POSITIONS = 3
AQUISATE_SERVOS_DESTINATIONS = 4
AQUISATE_SERVOS_STATUS = 5

AQUISATE_CURRENT_VALUES = 6
AQUISATE_CURRENT_MAX = 7  # This was previously "CONSUMPTIONS"
AQUISATE_CURRENT_TOTAL = 8  # This was previously "MAX"


class LegControllerDataAquisator(DeviceAquisators):
    @classmethod
    def get_data_aquisators(cls):
        return super().get_data_aquisators() + [
            DataAquisator("servos positions", 10, AQUISATE_SERVOS_POSITIONS),
            DataAquisator("servos destinations", 10, AQUISATE_SERVOS_DESTINATIONS),
            DataAquisator("servos status", 10, AQUISATE_SERVOS_STATUS),
            DataAquisator("current actual", 10, AQUISATE_CURRENT_VALUES),
            DataAquisator("current max", 10, AQUISATE_CURRENT_MAX),
            DataAquisator("current total", 10, AQUISATE_CURRENT_TOTAL),
        ]
