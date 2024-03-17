from RoboControl.Robot.Device.control.DataAquisator import DataAquisator
from RoboControl.Robot.Device.control.DeviceAquisators import DeviceAquisators

MLX90614_AQUISATE_AMBIENT = 3
MLX90614_AQUISATE_OBJECT = 4
VCNL4000_AQUISATE_LUX = 5
VCNL4000_AQUISATE_DISTANCE = 6
BMP085_AQUISATE_TEMPERATURE = 7
BMP085_AQUISATE_PRESURE = 8
TMF8821_AQUISATE_DISTANCE = 9


class HeadSensorsDataAquisator(DeviceAquisators):
    @classmethod
    def get_data_aquisators(cls):
        return super().get_data_aquisators() + [
            # DataAquisator("Mxl90614 ambient temperature", 100, MLX90614_AQUISATE_AMBIENT),
            # DataAquisator("Mxl90614 object temperature", 100, MLX90614_AQUISATE_OBJECT),
            #DataAquisator("VCNL4000 lux", 100, VCNL4000_AQUISATE_LUX),
            #DataAquisator("VCNL4000 distance", 100, VCNL4000_AQUISATE_DISTANCE),
            # DataAquisator("Bmp085 temperature", 10, BMP085_AQUISATE_TEMPERATURE),
            # DataAquisator("Bmp085 pressure", 10, BMP085_AQUISATE_PRESURE),
            DataAquisator("TMF8821 distance", 100, TMF8821_AQUISATE_DISTANCE),
        ]
