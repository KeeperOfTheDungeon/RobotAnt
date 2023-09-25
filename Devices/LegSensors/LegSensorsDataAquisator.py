from RoboControl.Robot.Device.control.DataAquisator import DataAquisator
from RoboControl.Robot.Device.control.DeviceAquisators import DeviceAquisators

VCNL4000_AQUISATE_LUX = 3
VCNL4000_AQUISATE_DISTANCE = 4


class LegSensorsDataAquisator(DeviceAquisators):
    @classmethod
    def get_data_aquisators(cls):
        return super().get_data_aquisators() + [
            DataAquisator("VCNL4000 lux", 100, VCNL4000_AQUISATE_LUX),
            DataAquisator("VCNL4000 distance", 100, VCNL4000_AQUISATE_DISTANCE),
        ]
