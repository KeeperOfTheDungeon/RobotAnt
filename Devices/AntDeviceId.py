
#from RoboControl.Robot.AbstractRobot.AbstractDeviceConfig import AbstractDeviceConfig
from RoboControl.Robot.AbstractRobot.Config.DeviceConfig import DeviceConfig

class AntDeviceConfig(DeviceConfig):

	MAIN_DATA_HUB_ID = 0
	LEG_CONTROLLER_ID = 10
	HEAD_SENSORS_ID = 11
	LEG_SENSORS_ID = 13

	MAIN_DATA_HUB = DeviceConfig(0 ,"main data hub")
	LEG_CONTROLLER = DeviceConfig(10 ," leg controller")
	HEAD_SENSORS = DeviceConfig(11,"head sensors")
	LEG_SENSORS = DeviceConfig(13,"leg sensors")





"""package de.hska.lat.ant_IIIb.metaData;

import de.hska.lat.robot.device.DeviceMetaData;

public enum AntDeviceId
{
	MAIN_DATA_HUB (0,"main data hub"),
	LEG_CONTROLLER (10," leg controller"),
	HEAD_SENSORS (11,"head sensors"),
	TAIL_BOARD (12,"tail board"),
	LEG_SENSORS (13,"leg sensors"),
	IR_COM (14,"ir com"),
	PIXY_CONTROLLER (42,"pixy Controller")
	
	;
	
	/**
	 * @uml.property  name="id"
	 */
	private final byte id;
	/**
	 * @uml.property  name="name"
	 */
	private final String name;
	
private AntDeviceId(int id,String name)
{
	this.id=(byte)id;
	this.name=name;
}
	
/**
 * @return
 * @uml.property  name="id"
 */
public byte getId()
{
	return(id);
}
	
/**
 * @return
 * @uml.property  name="name"
 */
public String getName()
{
	return(this.name);
}


public DeviceMetaData getDeviceMetaData()
{
	return(new DeviceMetaData(this.name,this.id));
}



}
"""