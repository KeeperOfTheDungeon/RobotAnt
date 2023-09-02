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
STREAM_CURRENT_TOTAL_CONSUMPTION = 0x25
STREAM_CURRENT_MAX_CONSUMPTION = 0x24
STREAM_SERVO_RAW_ANALOG_VALUES = 0x26
STREAM_TEMPERATURES = 0x27


class LegControllerProtocol(DeviceProtocol):
    def get_servo_protocol(self):
        protocol = {
            "device_id": self._device_id,
            "cmd_setSettings": CMD_SERVO_SET_SETTINGS,
            "cmd_getSettings": CMD_SERVO_GET_SETTINGS,
            "cmd_saveDefaults": CMD_SERVO_SAVE_DEFAULTS,
            "cmd_loadDefaults": CMD_SERVO_LOAD_DEFAULTS,
            "cmd_getValue": CMD_SERVO_GET_VALUE,
            "msg_settings": MSG_SERVO_SETTINGS,

            "cmd_servoOn": CMD_SERVO_ON,
            "cmd_servoOff": CMD_SERVO_OFF,

            "cmd_getServoStatus": CMD_GET_SERVO_STATUS,
            "cmd_getServoPosition": CMD_GET_SERVO_POSITION,
            "cmd_getServoSpeed": CMD_GET_SERVO_SPEED,

            "cmd_moveServoTo": CMD_SERVO_MOVE_TO,
            "cmd_servoMoveToAtSpeed": CMD_SERVO_MOVE_TO_AT_SPEED,

            "cmd_setServoPosition": CMD_SET_SERVO_POSITION,
            "cmd_setServoSpeed": CMD_SET_SERVO_SPEED,

            "cmd_servoMove": CMD_SERVO_MOVE,
            "cmd_calibrateServo": CMD_CALIBRATE_SERVO,
            "stream_servoSaw_analog_values": STREAM_SERVO_RAW_ANALOG_VALUES,
            "stream_servoPositions": STREAM_SERVOS_POSITIONS,
            "stream_servoDestinations": STREAM_SERVOS_DESTINATIONS
        }

        return protocol

    def get_current_protocol(self):
        protocol = {
            "device_id": self._device_id,
            "cmd_setSettings": CMD_CURRENT_SET_SETTINGS,
            "cmd_getSettings": CMD_CURRENT_GET_SETTINGS,
            "cmd_saveDefaults": CMD_CURRENT_SAVE_DEFAULTS,
            "cmd_loadDefaults": CMD_CURRENT_LOAD_DEFAULTS,
            "cmd_getValue": CMD_CURRENT_GET_VALUE,  # same as CMD_GET_ACTUAL_CURRENT_DRAIN ?
            "msg_settings": MSG_CURRENT_SETTINGS,

            "cmd_getTotalCurrent": CMD_GET_TOTAL_CURRENT_DRAIN,
            "cmd_resetTotalCurrent": CMD_RESET_TOTAL_CURRENT_DRAIN,

            "cmd_getMaxCurrent": CMD_GET_MAXIMAL_CURRENT_DRAIN,
            "cmd_resetMaxCurrent": CMD_RESET_MAXIMAL_CURRENT_DRAIN,

            "msg_actualCurrent": MSG_CURRENT_VALUE,
            "msg_totalCurrent": MSG_CURRENT_TOTAL_CONSUMPTION,
            "msg_maxCurrent": MSG_CURRENT_MAX_VALUE,

            "stream_actualCurrent": STREAM_CURRENT_CONSUMPTION,
            "stream_totalCurrent": STREAM_CURRENT_TOTAL_CONSUMPTION,
            "stream_maxCurrent": STREAM_CURRENT_MAX_CONSUMPTION
        }

        return protocol


"""package de.hska.lat.ant_IIIb.devices.legController;




import de.hska.lat.robot.component.generic.motion.MotionProtocol2D;
import de.hska.lat.robot.component.sensor.lm75.Lm75Protocol;
import de.hska.lat.robot.component.actor.servo.feedbackServo.protocol.Stream_servoRawAnalogPosition;
import de.hska.lat.robot.component.actor.servo.forceFeedback.protocol.ForceFeedbackServoProtocol;
import de.hska.lat.robot.component.actor.servo.protocol.Msg_servoPosition;
import de.hska.lat.robot.component.actor.servo.protocol.Msg_servoSettings;
import de.hska.lat.robot.component.actor.servo.protocol.Msg_servoSpeed;
import de.hska.lat.robot.component.actor.servo.protocol.Stream_servosDestinations;
import de.hska.lat.robot.component.actor.servo.protocol.Stream_servosPositions;
import de.hska.lat.robot.component.actor.servo.protocol.Stream_servosStatus;
import de.hska.lat.robot.component.currentSensor.CurrentSensorProtocol;
import de.hska.lat.robot.device.protocol.DeviceProtocol;
import de.hska.lat.robot.device.device.remoteProcessor.RemoteMessageProcessor;
import de.hska.lat.robot.device.device.remoteProcessor.RemoteStreamProcessor;



public class LegControllerProtocol extends DeviceProtocol
{
    
    

    public static final byte CMD_SERVO_SET_SETTINGS	= 0x20;
    public static final byte CMD_SERVO_GET_SETTINGS = 0x21;
    public static final byte CMD_SERVO_SAVE_DEFAULTS = 0x22;
    public static final byte CMD_SERVO_LOAD_DEFAULTS = 0x23;
    
    
    public static final byte CMD_SERVO_ON = 0x24;
    public static final byte CMD_SERVO_OFF = 0x25;
    

    public static final byte CMD_SERVO_MOVE_TO = 0x26;
    public static final byte CMD_SERVO_MOVE_TO_AT_SPEED = 0x27;
    public static final byte CMD_SERVO_MOVE = 0x28;
    
    public static final byte CMD_SET_SERVO_POSITION = 0x29;
    public static final byte CMD_GET_SERVO_POSITION = 0x2A;
    public static final byte CMD_SET_SERVO_SPEED = 0x2B;
    public static final byte CMD_GET_SERVO_SPEED = 0x2C;

    
    public static final byte CMD_GET_SERVO_STATUS = 0x2D;	

    public static final byte CMD_CALIBRATE_SERVO = 0x2E;
    
    public static final byte CMD_CURRENT_SET_SETTINGS 					= 0x40;
    public static final byte CMD_CURRENT_GET_SETTINGS					= 0x41;
    public static final byte CMD_CURRENT_LOAD_DEFAULTS					= 0x42; 
    public static final byte CMD_CURRENT_SAVE_DEFAULTS					= 0x43;
    
    public static final byte CMD_GET_ACTUAL_CURRENT_DRAIN				= 0x44;
    
    
    public static final byte CMD_GET_TOTAL_CURRENT_DRAIN				= 0x46;
    public static final byte CMD_RESET_TOTAL_CURRENT_DRAIN				= 0x47;
        
    public static final byte CMD_GET_MAXIMAL_CURRENT_DRAIN				= 0x45;
    public static final byte CMD_RESET_MAXIMAL_CURRENT_DRAIN			= 0x47;
    
    
    
    public static final byte CMD_TEMPERATURE_SET_SETTINGS 					= 0x50;
    public static final byte CMD_TEMPERATURE_GET_SETTINGS					= 0x51;
    public static final byte CMD_TEMPERATURE_LOAD_DEFAULTS					= 0x52; 
    public static final byte CMD_TEMPERATURE_SAVE_DEFAULTS					= 0x53;
    public static final byte CMD_GET_TEMPERATURE							= 0x54;
        

    
    public static final byte MSG_SERVO_SETTINGS 						= 0x20;
    public static final byte MSG_SERVO_POSITION							= 0x21;
    public static final byte MSG_SERVO_SPEED 							= 0x22;
    public static final byte MSG_SERVO_STATUS 							= 0x23;
    

    
    
    
    public static final byte MSG_CURRENT_VALUE			= 0x30;

    public static final byte MSG_CURRENT_MAX_VALUE		= 0x32;


    public static final byte MSG_CURRENT_TOTAL_CONSUMPTION	= 0x34;

    public static final byte MSG_CURRENT_SETTINGS		= 0x36;
    
    
    public static final byte MSG_TEMPERATURE_VALUE		=	0x3a;
    public static final byte MSG_TEMPERATURE_SETTINGS	=	0x3b;
    
    
    
    
    public static final byte STREAM_SERVOS_POSITIONS 				= 0x20;
    public static final byte STREAM_SERVOS_DESTINATIONS 			= 0x21;
    public static final byte STREAM_SERVOS_STATUS	 				= 0x22;

    public static final byte STREAM_CURRENT_CONSUMPTION 			= 0x23;
    public static final byte STREAM_CURRENT_TOTAL_CONSUMPTION		= 0x24;
    public static final byte STREAM_CURRENT_MAX_CONSUMPTION		 	= 0x25;
    public static final byte STREAM_SERVO_RAW_ANALOG_VALUES		 	= 0x26;	
    public static final byte STREAM_TEMPERATURES		 			= 0x27;

public LegControllerProtocol(LegController device)
{
    super(device);
    

    
     this.messageList.add(new RemoteMessageProcessor(new Msg_servoSettings(LegControllerProtocol.MSG_SERVO_SETTINGS),device.getServos()));
     this.messageList.add(new RemoteMessageProcessor(new Msg_servoPosition(LegControllerProtocol.MSG_SERVO_POSITION),device.getServos()));
     this.messageList.add(new RemoteMessageProcessor(new Msg_servoSpeed(LegControllerProtocol.MSG_SERVO_SPEED),device.getServos()));
    
     
     
     
     this.streamList.add(new RemoteStreamProcessor(new Stream_servosPositions(LegControllerProtocol.STREAM_SERVOS_POSITIONS), device.getServos()));
     this.streamList.add(new RemoteStreamProcessor(new Stream_servosDestinations(LegControllerProtocol.STREAM_SERVOS_DESTINATIONS), device.getServos()));
     this.streamList.add(new RemoteStreamProcessor(new Stream_servosStatus(LegControllerProtocol.STREAM_SERVOS_STATUS), device.getServos()));
     this.streamList.add(new RemoteStreamProcessor(new Stream_servoRawAnalogPosition(LegControllerProtocol.STREAM_SERVO_RAW_ANALOG_VALUES), device.getServos()));
    
     
     this.streamList.addAll(LegControllerProtocol.getCurrentProtocol(device.getId()).getStreamProcessors(device.getCurrentSensors()));
     this.streamList.addAll(LegControllerProtocol.getTemperatureProtocol(device.getId()).getStreamProcessors(device.getTemperatureSensors()));
     
     
     this.messageList.addAll(LegControllerProtocol.getCurrentProtocol(device.getId()).getMessageProcessors(device.getCurrentSensors()));
     this.messageList.addAll(LegControllerProtocol.getTemperatureProtocol(device.getId()).getMessageProcessors(device.getTemperatureSensors()));
     


     //getCommandProcessors
}
    
    
public static ForceFeedbackServoProtocol getServoProtocol(int deviceId)
{	
    ForceFeedbackServoProtocol servoProtocol;
    
    servoProtocol = new ForceFeedbackServoProtocol(
             deviceId,
             LegControllerProtocol.CMD_SERVO_SET_SETTINGS,
             LegControllerProtocol.CMD_SERVO_GET_SETTINGS,
             LegControllerProtocol.CMD_SERVO_SAVE_DEFAULTS,
             LegControllerProtocol.CMD_SERVO_LOAD_DEFAULTS,
             LegControllerProtocol.MSG_SERVO_SETTINGS,
             
            
             
             LegControllerProtocol.CMD_SERVO_ON,
             LegControllerProtocol.CMD_SERVO_OFF,
             
              0, 0, 0, 0,
             
              LegControllerProtocol.CMD_GET_SERVO_STATUS,
             LegControllerProtocol.CMD_GET_SERVO_POSITION,
             LegControllerProtocol.CMD_GET_SERVO_SPEED,
             
             
             LegControllerProtocol.CMD_SERVO_MOVE_TO,
             LegControllerProtocol.CMD_SERVO_MOVE_TO_AT_SPEED,
             
             LegControllerProtocol.CMD_SET_SERVO_POSITION,
             LegControllerProtocol.CMD_SET_SERVO_SPEED,  0,0,0,0,
             
             
             LegControllerProtocol.CMD_SERVO_MOVE,
             LegControllerProtocol.CMD_CALIBRATE_SERVO,
             LegControllerProtocol.STREAM_SERVO_RAW_ANALOG_VALUES
             
             );
    
    
    return (servoProtocol);
}



public static CurrentSensorProtocol getCurrentProtocol(int deviceId)
{

    CurrentSensorProtocol currentProtocol;
    
     currentProtocol = new CurrentSensorProtocol(deviceId,
             LegControllerProtocol.CMD_CURRENT_SET_SETTINGS,
             LegControllerProtocol.CMD_CURRENT_GET_SETTINGS,
             LegControllerProtocol.CMD_CURRENT_SAVE_DEFAULTS,
             LegControllerProtocol.CMD_CURRENT_LOAD_DEFAULTS,
             LegControllerProtocol.MSG_CURRENT_SETTINGS,
             
             LegControllerProtocol.CMD_GET_ACTUAL_CURRENT_DRAIN,
             LegControllerProtocol.MSG_CURRENT_VALUE,
             LegControllerProtocol.STREAM_CURRENT_CONSUMPTION ,
             
             
             LegControllerProtocol.CMD_GET_TOTAL_CURRENT_DRAIN,
             LegControllerProtocol.CMD_RESET_TOTAL_CURRENT_DRAIN,
             LegControllerProtocol.MSG_CURRENT_TOTAL_CONSUMPTION,
             LegControllerProtocol.STREAM_CURRENT_TOTAL_CONSUMPTION,
             
             LegControllerProtocol.CMD_GET_MAXIMAL_CURRENT_DRAIN,
             LegControllerProtocol.CMD_RESET_MAXIMAL_CURRENT_DRAIN,
            
             LegControllerProtocol.MSG_CURRENT_MAX_VALUE,
             LegControllerProtocol.STREAM_CURRENT_MAX_CONSUMPTION
             
             );
    /*

        public static final byte STREAM_CURRENT_TOTAL_CONSUMPTION		= 0x24;
        public static final byte STREAM_CURRENT_MAX_CONSUMPTION		 	= 0x25;	
        */
    return (currentProtocol);

}


public static MotionProtocol2D getMotionProtocol(int deviceId)
{
    MotionProtocol2D protocol;
     
     protocol = new MotionProtocol2D(deviceId, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);

    return (protocol);
}


public static Lm75Protocol getTemperatureProtocol(int deviceId)
{
    Lm75Protocol protocol;
     
     protocol = new Lm75Protocol(deviceId,
             
             LegControllerProtocol.CMD_TEMPERATURE_SET_SETTINGS,
             LegControllerProtocol.CMD_TEMPERATURE_GET_SETTINGS,
             LegControllerProtocol.CMD_TEMPERATURE_SAVE_DEFAULTS,
             LegControllerProtocol.CMD_TEMPERATURE_LOAD_DEFAULTS,
             LegControllerProtocol.MSG_TEMPERATURE_SETTINGS,
             LegControllerProtocol.CMD_GET_TEMPERATURE, 
             LegControllerProtocol.MSG_TEMPERATURE_VALUE,
             
             LegControllerProtocol.STREAM_TEMPERATURES);

    return (protocol);
}






    
}
"""
