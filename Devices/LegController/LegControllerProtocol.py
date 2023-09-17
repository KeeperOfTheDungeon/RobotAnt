from RoboControl.Robot.Device.Protocol.DeviceProtocol import DeviceProtocol

CMD_SERVO_SET_SETTINGS = 0x20
CMD_SERVO_GET_SETTINGS = 0x21
CMD_SERVO_SAVE_DEFAULTS = 0x22
CMD_SERVO_LOAD_DEFAULTS = 0x23
CMD_SERVO_GET_VALUE = 0

CMD_SERVO_ON = 0x24
CMD_SERVO_OFF = 0x25

CMD_SERVO_MOVE_TO = 0x26
CMD_SERVO_MOVE_TO_AT_SPEED = 0x27
CMD_SERVO_MOVE = 0x28

CMD_SET_SERVO_POSITION = 0x29
CMD_GET_SERVO_POSITION = 0x2A
CMD_SET_SERVO_SPEED = 0x2B
CMD_GET_SERVO_SPEED = 0x2C

CMD_GET_SERVO_STATUS = 0x2D

CMD_CALIBRATE_SERVO = 0x2E

CMD_CURRENT_SET_SETTINGS = 0x40
CMD_CURRENT_GET_SETTINGS = 0x41
CMD_CURRENT_LOAD_DEFAULTS = 0x42
CMD_CURRENT_SAVE_DEFAULTS = 0x43
CMD_CURRENT_GET_VALUE = 0x44
CMD_GET_ACTUAL_CURRENT_DRAIN = 0x44  # TODO same as GET_VALUE ?

CMD_GET_TOTAL_CURRENT_DRAIN = 0x46
CMD_RESET_TOTAL_CURRENT_DRAIN = 0x47

CMD_GET_MAXIMAL_CURRENT_DRAIN = 0x45
CMD_RESET_MAXIMAL_CURRENT_DRAIN = 0x47

CMD_TEMPERATURE_SET_SETTINGS = 0x50
CMD_TEMPERATURE_GET_SETTINGS = 0x51
CMD_TEMPERATURE_LOAD_DEFAULTS = 0x52
CMD_TEMPERATURE_SAVE_DEFAULTS = 0x53
CMD_GET_TEMPERATURE = 0x54

MSG_SERVO_SETTINGS = 0x20
MSG_SERVO_POSITION = 0x21
MSG_SERVO_SPEED = 0x22
MSG_SERVO_STATUS = 0x23

MSG_CURRENT_VALUE = 0x30

MSG_CURRENT_MAX_VALUE = 0x32

MSG_CURRENT_TOTAL_CONSUMPTION = 0x34

MSG_CURRENT_SETTINGS = 0x36

MSG_TEMPERATURE_VALUE = 0x3a
MSG_TEMPERATURE_SETTINGS = 0x3b

STREAM_SERVOS_POSITIONS = 0x20
STREAM_SERVOS_DESTINATIONS = 0x21
STREAM_SERVOS_STATUS = 0x22

STREAM_CURRENT_CONSUMPTION = 0x23
# FIXME This is different than the Java source
STREAM_CURRENT_TOTAL_CONSUMPTION = 0x25  # public static final byte STREAM_CURRENT_TOTAL_CONSUMPTION		= 0x24;
# FIXME This is different than the Java source
STREAM_CURRENT_MAX_CONSUMPTION = 0x24  # public static final byte STREAM_CURRENT_MAX_CONSUMPTION		 	= 0x25;

STREAM_SERVO_RAW_ANALOG_VALUES = 0x26
STREAM_TEMPERATURES = 0x27


class LegControllerProtocol(DeviceProtocol):
    def __init__(self, *args):
        super().__init__(*args)

        # FIXME why here ?
        # self._message_list.append(RemoteMessageProcessor(Msg_servoSettings(LegControllerProtocol.MSG_SERVO_SETTINGS),device.get_servos()));
        # self._message_list.append(RemoteMessageProcessor(Msg_servoPosition(LegControllerProtocol.MSG_SERVO_POSITION),device.get_servos()));
        # self._message_list.append(RemoteMessageProcessor(Msg_servoSpeed(LegControllerProtocol.MSG_SERVO_SPEED),device.get_servos()));
        # self._stream_list.append(RemoteStreamProcessor(Stream_servosPositions(LegControllerProtocol.STREAM_SERVOS_POSITIONS), device.get_servos()));
        # self._stream_list.append(RemoteStreamProcessor(Stream_servosDestinations(LegControllerProtocol.STREAM_SERVOS_DESTINATIONS), device.get_servos()));
        # self._stream_list.append(RemoteStreamProcessor(Stream_servosStatus(LegControllerProtocol.STREAM_SERVOS_STATUS), device.get_servos()));
        # self._stream_list.append(RemoteStreamProcessor(Stream_servoRawAnalogPosition(LegControllerProtocol.STREAM_SERVO_RAW_ANALOG_VALUES), device.get_servos()));
        # 
        # self._stream_list.append(LegControllerProtocol.getCurrentProtocol(device.getId()).getStreamProcessors(device.getCurrentSensors()));
        # self._stream_list.append(LegControllerProtocol.getTemperatureProtocol(device.getId()).getStreamProcessors(device.getTemperatureSensors()));
        # self._message_list.append(LegControllerProtocol.getCurrentProtocol(device.getId()).getMessageProcessors(device.getCurrentSensors()));
        # self._message_list.append(LegControllerProtocol.getTemperatureProtocol(device.getId()).getMessageProcessors(device.getTemperatureSensors()));

    def get_servo_protocol(self):  # ForceFeedbackServoProtocol
        protocol = {
            "device_id": self._device_id,
            "cmd_setSettings": CMD_SERVO_SET_SETTINGS,
            "cmd_getSettings": CMD_SERVO_GET_SETTINGS,
            "cmd_saveDefaults": CMD_SERVO_SAVE_DEFAULTS,
            "cmd_loadDefaults": CMD_SERVO_LOAD_DEFAULTS,
            "msg_settings": MSG_SERVO_SETTINGS,
            "cmd_getValue": CMD_SERVO_GET_VALUE,

            "cmd_servoOn": CMD_SERVO_ON,
            "cmd_servoOff": CMD_SERVO_OFF,

            # 0, 0, 0, 0,

            "cmd_get_servostatus": CMD_GET_SERVO_STATUS,
            "cmd_getServoPosition": CMD_GET_SERVO_POSITION,
            "cmd_get_servospeed": CMD_GET_SERVO_SPEED,

            "cmd_moveServoTo": CMD_SERVO_MOVE_TO,
            "cmd_servoMoveToAtSpeed": CMD_SERVO_MOVE_TO_AT_SPEED,

            "cmd_setServoPosition": CMD_SET_SERVO_POSITION,
            "cmd_setServoSpeed": CMD_SET_SERVO_SPEED,

            # 0,0,0,0,

            "cmd_servoMove": CMD_SERVO_MOVE,
            "cmd_calibrateServo": CMD_CALIBRATE_SERVO,
            "stream_servoSaw_analog_values": STREAM_SERVO_RAW_ANALOG_VALUES,

            "stream_servoPositions": STREAM_SERVOS_POSITIONS,
            "stream_servoDestinations": STREAM_SERVOS_DESTINATIONS,
        }

        return protocol

    def get_current_protocol(self):
        protocol = {
            "device_id": self._device_id,
            "cmd_setSettings": CMD_CURRENT_SET_SETTINGS,
            "cmd_getSettings": CMD_CURRENT_GET_SETTINGS,
            "cmd_saveDefaults": CMD_CURRENT_SAVE_DEFAULTS,
            "cmd_loadDefaults": CMD_CURRENT_LOAD_DEFAULTS,
            "msg_settings": MSG_CURRENT_SETTINGS,
            "cmd_getActualCurrentDrain": CMD_GET_ACTUAL_CURRENT_DRAIN,
            "cmd_getValue": CMD_CURRENT_GET_VALUE,  # same as CMD_GET_ACTUAL_CURRENT_DRAIN ?

            "cmd_getTotalCurrent": CMD_GET_TOTAL_CURRENT_DRAIN,
            "cmd_resetTotalCurrent": CMD_RESET_TOTAL_CURRENT_DRAIN,

            "cmd_getMaxCurrent": CMD_GET_MAXIMAL_CURRENT_DRAIN,
            "cmd_resetMaxCurrent": CMD_RESET_MAXIMAL_CURRENT_DRAIN,

            "msg_actualCurrent": MSG_CURRENT_VALUE,
            "msg_totalCurrent": MSG_CURRENT_TOTAL_CONSUMPTION,
            "msg_maxCurrent": MSG_CURRENT_MAX_VALUE,

            "stream_actualCurrent": STREAM_CURRENT_CONSUMPTION,
            "stream_totalCurrent": STREAM_CURRENT_TOTAL_CONSUMPTION,
            "stream_maxCurrent": STREAM_CURRENT_MAX_CONSUMPTION,
        }

        return protocol

    # def get_motion_protocol(self) -> "MotionProtocol2D":
    #     return MotionProtocol2D(self._device_id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    def get_temperature_protocol(self) -> dict:
        return {
            "device_id": self._device_id,
            "cmd_setSettings": CMD_TEMPERATURE_SET_SETTINGS,
            "cmd_getSettings": CMD_TEMPERATURE_GET_SETTINGS,
            "cmd_saveDefaults": CMD_TEMPERATURE_SAVE_DEFAULTS,
            "cmd_loadDefaults": CMD_TEMPERATURE_LOAD_DEFAULTS,
            "msg_settings": MSG_TEMPERATURE_SETTINGS,
            "cmd_getTemperature": CMD_GET_TEMPERATURE,
            "msg_temperatureValue": MSG_TEMPERATURE_VALUE,
            "stream_temperatures:": STREAM_TEMPERATURES,
        }
