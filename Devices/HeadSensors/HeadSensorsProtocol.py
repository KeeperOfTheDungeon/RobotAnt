from RoboControl.Robot.Component.Actor.Led.LedProtocol import LedProtocol
from RoboControl.Robot.Device.Protocol.DeviceProtocol import DeviceProtocol
from RoboControl.Robot.Device.remoteProcessor.RemoteProcessor import RemoteProcessor

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


class HeadSensorsProtocol(DeviceProtocol):

    def __init__(self, device):
        super().__init__(device)

        # self._remote_stream_processor_list.extend

        """		self._remote_stream_processor_list.append(RemoteProcessor(Stream_comStatistics(STREAM_COM_STATISTICS),device) )
        self._remote_stream_processor_list.append(RemoteProcessor(Stream_cpuStatistics(STREAM_CPU_STATISTICS),device) )


        self._remote_command_processor_list.append(RemoteProcessor(Cmd_ping(CMD_PING),device) )
        self._remote_command_processor_list.append(RemoteProcessor(Cmd_getNodeId(CMD_GET_NODE_ID),device) )

        self._remote_message_processor_list.append(RemoteProcessor(Msg_pingResponse(),device) )
        """

    #		 this.streamList.addAll(LegSensorsProtocol.getVcnl4000Protocol(device.getId()).getStreamProcessors(device.getVcnl4000Set()));
    # this.messageList.addAll(LegSensorsProtocol.getVcnl4000Protocol(device.getId()).getMessageProcessors(device.getVcnl4000Set()));

    #		self._remote_stream_processor_list.append(RemoteProcessor(Stream_comStatistics(STREAM_COM_STATISTICS),device) )
    #		self._remote_stream_processor_list.append(RemoteProcessor(Stream_cpuStatistics(STREAM_CPU_STATISTICS),device) )

    def get_vcnl4000_protocol(self):
        protocol = {"device_id": self._device_id,
                    "cmd_setSettings": CMD_VCNL4020_SET_SETTINGS,
                    "cmd_getSettings": CMD_VCNL4020_GET_SETTINGS,
                    "cmd_saveDefaults": CMD_VCNL4020_SAVE_DEFAULTS,
                    "cmd_loadDefaults": CMD_VCNL4020_LOAD_DEFAULTS,
                    "cmd_getValue": CMD_VCNL4020_GET_VALUE,
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
                    "msg_distanceTable": MSG_VCNL4020_DISTANCE_TABLE}

        return protocol


"""
package de.hska.lat.ant_IIIb.devices.headSensors;









import de.hska.lat.robot.component.temperatureSensor.mlx90614.Mlx90614Protocol;


import de.hska.lat.robot.component.sensor.bmp085.Bmp085Protocol;

import de.hska.lat.robot.component.sensor.vcnl4000.Vcnl4000Protocol;

import de.hska.lat.robot.device.protocol.DeviceProtocol;



public class HeadSensorsProtocol extends DeviceProtocol
{
    

    

    
    
    
    
    public static final byte CMD_MLX90614_SET_SETTINGS				= 0x20;
    public static final byte CMD_MLX90614_GET_SETTINGS				= 0x21;
    public static final byte CMD_MLX90614_SAVE_DEFAULTS				= 0x22;
    public static final byte CMD_MLX90614_LOAD_DEFAULTS				= 0x23;
    public static final byte CMD_MLX90614_GET_AMBIENT_TEMPERATURE	= 0x24;
    public static final byte CMD_MLX90614_GET_OBJECT_TEMPERATURE	= 0x25;
    
    
    
    
    
    public static final byte CMD_VCNL4000_SET_SETTINGS				= 0x26;
    public static final byte CMD_VCNL4000_GET_SETTINGS				= 0x27;
    public static final byte CMD_VCNL4000_SAVE_DEFAULTS				= 0x28;
    public static final byte CMD_VCNL4000_LOAD_DEFAULTS				= 0x29;
    public static final byte CMD_VCNL4000_GET_LUX					= 0x2A;
    public static final byte CMD_VCNL4000_GET_DISTANCE				= 0x2B;

    
    public static final byte CMD_VCNL4000_GET_RAW_PROXIMITY 		= 0x2C;
    
    public static final byte CMD_VCNL4000_SET_DISTANCE_TABLE		= 0x2D;
    public static final byte CMD_VCNL4000_GET_DISTANCE_TABLE		= 0x2E;
    
    
    
    public static final byte CMD_BMP085_SET_SETTINGS				= 0x2F;
    public static final byte CMD_BMP085_GET_SETTINGS				= 0x30;
    public static final byte CMD_BMP085_SAVE_DEFAULTS				= 0x31;
    public static final byte CMD_BMP085_LOAD_DEFAULTS				= 0x32;
    public static final byte CMD_BMP085_GET_TEMPERATURE				= 0x33;
    public static final byte CMD_BMP085_GET_PRESURE					= 0x34;

    




    
    
    public static final byte MSG_MLX90614_SETTINGS					= 0x20;
    public static final byte MSG_MLX90614_AMBIENT_TEMPERATURE		= 0x21;
    public static final byte MSG_MLX90614_OBJECT_TEMPERATURE		= 0x22;
    

    
    public static final byte MSG_VCNL4000_SETTINGS					= 0x23;
    public static final byte MSG_VCNL4000_DISTANCE					= 0x24;
    public static final byte MSG_VCNL4000_DISTANCE_TABLE			= 0x25;
    public static final byte MSG_VCNL4000_LUX						= 0x26;
    public static final byte MSG_VCNL4000_RAW_PROXIMITY				= 0x27; 

    public static final byte MSG_BMP085_SETTINGS					= 0x28;
    public static final byte MSG_BMP085_TEMPERATURE					= 0x29;
    public static final byte MSG_BMP085_PRESURE						= 0x2A;

    
    
    
    public static final byte STREAM_MLX90614_AMBIENT_TEMPERATURES	= 0x20;
    public static final byte STREAM_MLX90614_OBJECT_TEMPERATURES	= 0x21;
    
    

    public static final byte STREAM_VCNL4000LUX_VALUES				= 0x22;
    public static final byte STREAM_VCNL4000DISTANCE_VALUES			= 0x23;

    
    public static final byte STREAM_BMP085_TEMPERATURES				= 0x24;
    public static final byte STREAM_BMP085_PRESURES					= 0x25;
    
    
    
    

    public HeadSensorsProtocol(HeadSensors device) 
    {
        
        super(device);
        
    

         
         this.messageList.addAll(HeadSensorsProtocol.getMlx90614Protocol(device.getId()).getMessageProcessors(device.getMlx90614Set()));
         this.streamList.addAll(HeadSensorsProtocol.getMlx90614Protocol(device.getId()).getStreamProcessors(device.getMlx90614Set()));
         
         this.messageList.addAll(HeadSensorsProtocol.getVcnl4000Protocol(device.getId()).getMessageProcessors(device.getVcnl4000Set()));
         this.streamList.addAll(HeadSensorsProtocol.getVcnl4000Protocol(device.getId()).getStreamProcessors(device.getVcnl4000Set()));
                 
    /*	 
         this.messageList.addAll(HeadSensorsProtocol.getBmp085Protocol(device.getId()).getMessageProcessors(device.getBmp085Set()));
         this.streamList.addAll(HeadSensorsProtocol.getBmp085Protocol(device.getId()).getStreamProcessors(device.getBmp085Set()));
*/
         
                     
                 

         

         
    }


    public static Mlx90614Protocol getMlx90614Protocol(int deviceId)
    {
        Mlx90614Protocol protocol;

        protocol = new Mlx90614Protocol(
                deviceId,
                HeadSensorsProtocol.CMD_MLX90614_SET_SETTINGS,
                HeadSensorsProtocol.CMD_MLX90614_GET_SETTINGS,
                HeadSensorsProtocol.CMD_MLX90614_SAVE_DEFAULTS,
                HeadSensorsProtocol.CMD_MLX90614_LOAD_DEFAULTS,
                HeadSensorsProtocol.MSG_MLX90614_SETTINGS,
                
                HeadSensorsProtocol.CMD_MLX90614_GET_AMBIENT_TEMPERATURE,
                HeadSensorsProtocol.MSG_MLX90614_AMBIENT_TEMPERATURE,
                HeadSensorsProtocol.STREAM_MLX90614_AMBIENT_TEMPERATURES,
                
                
                HeadSensorsProtocol.CMD_MLX90614_GET_OBJECT_TEMPERATURE,
                HeadSensorsProtocol.MSG_MLX90614_OBJECT_TEMPERATURE,
                HeadSensorsProtocol.STREAM_MLX90614_OBJECT_TEMPERATURES
                
                );
        
        return (protocol);
    }


    

    public static Bmp085Protocol getBmp085Protocol(int deviceId)
    {
        Bmp085Protocol protocol;

        protocol = new Bmp085Protocol(deviceId,
                HeadSensorsProtocol.CMD_BMP085_SET_SETTINGS,
                HeadSensorsProtocol.CMD_BMP085_GET_SETTINGS,
                HeadSensorsProtocol.CMD_BMP085_SAVE_DEFAULTS,
                HeadSensorsProtocol.CMD_BMP085_LOAD_DEFAULTS,
                HeadSensorsProtocol.MSG_BMP085_SETTINGS,
                
                HeadSensorsProtocol.CMD_BMP085_GET_TEMPERATURE,
                HeadSensorsProtocol.MSG_BMP085_TEMPERATURE,
                HeadSensorsProtocol.STREAM_BMP085_TEMPERATURES,
                
                HeadSensorsProtocol.CMD_BMP085_GET_PRESURE,
                HeadSensorsProtocol.MSG_BMP085_PRESURE,
                HeadSensorsProtocol.STREAM_BMP085_PRESURES
                
                );
        
        return (protocol);
    }


    public static Vcnl4000Protocol getVcnl4000Protocol(int deviceId)
    {
        Vcnl4000Protocol protocol;

        protocol = new Vcnl4000Protocol(deviceId,
                HeadSensorsProtocol.CMD_VCNL4000_SET_SETTINGS,
                HeadSensorsProtocol.CMD_VCNL4000_GET_SETTINGS,
                HeadSensorsProtocol.CMD_VCNL4000_SAVE_DEFAULTS,
                HeadSensorsProtocol.CMD_VCNL4000_LOAD_DEFAULTS,
                HeadSensorsProtocol.MSG_VCNL4000_SETTINGS,
                
                HeadSensorsProtocol.CMD_VCNL4000_GET_LUX,
                HeadSensorsProtocol.MSG_VCNL4000_LUX,
                HeadSensorsProtocol.STREAM_VCNL4000LUX_VALUES,
                
                HeadSensorsProtocol.CMD_VCNL4000_GET_DISTANCE,
                HeadSensorsProtocol.MSG_VCNL4000_DISTANCE,
                HeadSensorsProtocol.STREAM_VCNL4000DISTANCE_VALUES,
                
                HeadSensorsProtocol.CMD_VCNL4000_GET_RAW_PROXIMITY, 
                HeadSensorsProtocol.MSG_VCNL4000_RAW_PROXIMITY, 
                HeadSensorsProtocol.CMD_VCNL4000_SET_DISTANCE_TABLE,
                HeadSensorsProtocol.CMD_VCNL4000_GET_DISTANCE_TABLE,
                HeadSensorsProtocol.MSG_VCNL4000_DISTANCE_TABLE
                );
        
        return (protocol);
    }



}


"""
