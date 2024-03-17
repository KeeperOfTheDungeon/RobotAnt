
from RoboControl.Robot.Device.DeviceProtocol import DeviceProtocol

from RoboControl.Robot.Device.RemoteProcessor import RemoteProcessor

CMD_VCNL4020_SET_SETTINGS = 0x26
CMD_VCNL4020_GET_SETTINGS = 0x27
CMD_VCNL4020_SAVE_DEFAULTS = 0x28
CMD_VCNL4020_LOAD_DEFAULTS = 0x29

CMD_VCNL4020_GET_VALUE = 0x0

CMD_VCNL4020_GET_LUX = 0x2A
CMD_VCNL4020_GET_DISTANCE = 0x2B

CMD_VCNL4020_GET_RAW_PROXIMITY = 0x2C

CMD_VCNL4020_SET_DISTANCE_TABLE = 0x2D
CMD_VCNL4020_GET_DISTANCE_TABLE = 0x2E

MSG_VCNL4020_SETTINGS = 0x23
MSG_VCNL4020_DISTANCE = 0x24
MSG_VCNL4020_DISTANCE_TABLE = 0x25
MSG_VCNL4020_LUX = 0x26
MSG_VCNL4020_RAW_PROXIMITY = 0x27

STREAM_VCNL4000LUX_VALUES = 0x22
STREAM_VCNL4000DISTANCE_VALUES = 0x23

CMD_MLX90614_SET_SETTINGS = 0x20
CMD_MLX90614_GET_SETTINGS = 0x21
CMD_MLX90614_SAVE_DEFAULTS = 0x22
CMD_MLX90614_LOAD_DEFAULTS = 0x23
CMD_MLX90614_GET_AMBIENT_TEMPERATURE = 0x24
CMD_MLX90614_GET_OBJECT_TEMPERATURE = 0x25

CMD_BMP085_SET_SETTINGS = 0x2F
CMD_BMP085_GET_SETTINGS = 0x30
CMD_BMP085_SAVE_DEFAULTS = 0x31
CMD_BMP085_LOAD_DEFAULTS = 0x32
CMD_BMP085_GET_TEMPERATURE = 0x33
CMD_BMP085_GET_PRESURE = 0x34

MSG_MLX90614_SETTINGS = 0x20
MSG_MLX90614_AMBIENT_TEMPERATURE = 0x21
MSG_MLX90614_OBJECT_TEMPERATURE = 0x22

MSG_VCNL4000_SETTINGS = 0x23
MSG_VCNL4000_DISTANCE = 0x24
MSG_VCNL4000_DISTANCE_TABLE = 0x25
MSG_VCNL4000_LUX = 0x26
MSG_VCNL4000_RAW_PROXIMITY = 0x27

MSG_BMP085_SETTINGS = 0x28
MSG_BMP085_TEMPERATURE = 0x29
MSG_BMP085_PRESURE = 0x2A

STREAM_MLX90614_AMBIENT_TEMPERATURES = 0x20
STREAM_MLX90614_OBJECT_TEMPERATURES = 0x21

STREAM_BMP085_TEMPERATURES = 0x24
STREAM_BMP085_PRESURES = 0x25

CMD_TMF882x_GET_DISTANCE = 0x20
CMD_TMF882x_GET_TEMPERATURE = 0x21
CMD_TMF882x_GET_VALUE = 0x0
CMD_TMF882x_SET_SETTINGS = 0x22
CMD_TMF882x_GET_SETTINGS = 0x23
CMD_TMF882x_SAVE_DEFAULTS = 0x24
CMD_TMF882x_LOAD_DEFAULTS = 0x25

MSG_TMF882x_DISTANCE = 0x20
MSG_TMF882x_TEMPERATURE = 0x21

STREAM_TMF882x_DISTANCE_VALUES = 0x20
STREAM_TMF882x_TEMPERATURE_VALUES = 0x21


class HeadSensorsProtocol(DeviceProtocol):
    def get_vcnl4020_protocol(self):
        protocol = {
            "device_id": self._device_id,
            "cmd_setSettings": CMD_VCNL4020_SET_SETTINGS,
            "cmd_getSettings": CMD_VCNL4020_GET_SETTINGS,
            "cmd_saveDefaults": CMD_VCNL4020_SAVE_DEFAULTS,
            "cmd_loadDefaults": CMD_VCNL4020_LOAD_DEFAULTS,
            "msg_settings": MSG_VCNL4020_SETTINGS,

            "cmd_getLux": CMD_VCNL4020_GET_LUX,
            "msg_lux": MSG_VCNL4020_LUX,
            "stream_lux": STREAM_VCNL4000LUX_VALUES,

            "cmd_getDistance": CMD_VCNL4020_GET_DISTANCE,
            "msg_distance": MSG_VCNL4020_DISTANCE,
            "stream_distance": STREAM_VCNL4000DISTANCE_VALUES,

            "cmd_getRawProximity": CMD_VCNL4020_GET_RAW_PROXIMITY,
            "msg_rawProximity": MSG_VCNL4020_RAW_PROXIMITY,
            "cmd_setDistanceTable": CMD_VCNL4020_SET_DISTANCE_TABLE,
            "cmd_getDistanceTable": CMD_VCNL4020_GET_DISTANCE_TABLE,
            "msg_distanceTable": MSG_VCNL4020_DISTANCE_TABLE,

            "cmd_getValue": CMD_VCNL4020_GET_VALUE,
        }

        return protocol

    def get_tmf882x_protocol(self):
        return {
            "device_id": self._device_id,
            "cmd_getDistance": CMD_TMF882x_GET_DISTANCE,
            "cmd_getTemperature": CMD_TMF882x_GET_TEMPERATURE,
            "cmd_setSettings": CMD_TMF882x_SET_SETTINGS,
            "cmd_getSettings": CMD_TMF882x_GET_SETTINGS,
            "cmd_saveDefaults": CMD_TMF882x_SAVE_DEFAULTS,
            "cmd_loadDefaults": CMD_TMF882x_LOAD_DEFAULTS,
            "cmd_getValue": CMD_TMF882x_GET_VALUE,
            "msg_distance": MSG_TMF882x_DISTANCE,
            "msg_temperature": MSG_TMF882x_TEMPERATURE,
            "stream_distance": STREAM_TMF882x_DISTANCE_VALUES,
            "stream_temperature": STREAM_TMF882x_TEMPERATURE_VALUES
        }

    def get_vcnl4000_protocol(self):
        protocol = self.get_vcnl4020_protocol()
        protocol.update({
            # "cmd_getRawProximity": CMD_VCNL4000_GET_RAW_PROXIMITY,
            "msg_rawProximity": MSG_VCNL4000_RAW_PROXIMITY,
            # "cmd_setDistanceTable": CMD_VCNL4000_SET_DISTANCE_TABLE,
            # "cmd_getDistanceTable": CMD_VCNL4000_GET_DISTANCE_TABLE,
            "msg_distanceTable": MSG_VCNL4000_DISTANCE_TABLE,
        })
        return protocol

    def get_mlx90614_protocol(self):
        protocol = {
            "device_id": self._device_id,
            "cmd_setSettings": CMD_MLX90614_SET_SETTINGS,
            "cmd_getSettings": CMD_MLX90614_GET_SETTINGS,
            "cmd_saveDefaults": CMD_MLX90614_SAVE_DEFAULTS,
            "cmd_loadDefaults": CMD_MLX90614_LOAD_DEFAULTS,
            "msg_settings": MSG_MLX90614_SETTINGS,

            "cmd_getAmbientTemperature": CMD_MLX90614_GET_AMBIENT_TEMPERATURE,
            "msg_ambientTemperature": MSG_MLX90614_AMBIENT_TEMPERATURE,
            "stream_ambientTemperatures": STREAM_MLX90614_AMBIENT_TEMPERATURES,

            "cmd_getObjectTemperature": CMD_MLX90614_GET_OBJECT_TEMPERATURE,
            "msg_objectTemperature": MSG_MLX90614_OBJECT_TEMPERATURE,
            "stream_objectTemperatures": STREAM_MLX90614_OBJECT_TEMPERATURES,
        }

        return protocol

    def get_bmp085_protocol(self):
        protocol = {
            "device_id": self._device_id,
            "cmd_setSettings": CMD_BMP085_SET_SETTINGS,
            "cmd_getSettings": CMD_BMP085_GET_SETTINGS,
            "cmd_saveDefaults": CMD_BMP085_SAVE_DEFAULTS,
            "cmd_loadDefaults": CMD_BMP085_LOAD_DEFAULTS,
            "msg_settings": MSG_BMP085_SETTINGS,

            "cmd_getTemperature": CMD_BMP085_GET_TEMPERATURE,
            "msg_temperature": MSG_BMP085_TEMPERATURE,
            "stream_temperatures": STREAM_BMP085_TEMPERATURES,

            "cmd_getPressure": CMD_BMP085_GET_PRESURE,
            "msg_pressure": MSG_BMP085_PRESURE,
            "stream_pressures": STREAM_BMP085_PRESURES,
        }

        return protocol
