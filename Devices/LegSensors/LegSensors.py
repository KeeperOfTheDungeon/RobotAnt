from Devices.LegSensors.LegSensorsLedSet import LegSensorsLedSet
from Devices.LegSensors.LegSensorsProtocol import LegSensorsProtocol
from Devices.LegSensors.LegSensorsVcnl4000 import LegSensorsVcnl4000
from RoboControl.Robot.Component.Actor.Led import Led
from RoboControl.Robot.Device.RobotDevice import RobotDevice


class LegSensors(RobotDevice):
	
	
	def __init__(self, component_config):
		super().__init__(component_config)


	def build(self):
		self._protocol = LegSensorsProtocol(self)

		protocol = self._protocol.get_led_protocol()
		self._led_set = LegSensorsLedSet(protocol)
		self.add_components(self._led_set)

		protocol = self._protocol.get_vcnl4000_protocol()
		self._vcnl_4000_set = LegSensorsVcnl4000(protocol)
		self.add_components(self._vcnl_4000_set)
		
		self.build_protocol()



	def build_protocol(self):
		super().build_protocol()
		
		
		self._remote_command_processor_list.extend(self._led_set.get_command_processors())
		self._remote_command_processor_list.extend(self._vcnl_4000_set.get_command_processors())

		self._remote_message_processor_list.extend(self._led_set.get_message_processors())
		self._remote_message_processor_list.extend(self._vcnl_4000_set.get_message_processors())
		
		self._remote_stream_processor_list.extend(self._led_set.get_stream_processors())
		self._remote_stream_processor_list.extend(self._vcnl_4000_set.get_stream_processors())
		


	def get_led_set(self):
		return self._led_set
		
	def get_vcnl_4000_set(self):
		return self._vcnl_4000_set

	def _load_setup(self):
		self._vcnl_4000_set.load_settings()


	def get_data_aquisators(self):
		aquisators = super().get_data_aquisators()
		aquisators.extend(["lux" ,
							"distance"])
		return aquisators

"""
public class LegSensors extends RobotDevice<DeviceEventNotifier, LegSensorsProtocol >
{
	
	
	/**
	 * @uml.property  name="vcnl4000set"
	 * @uml.associationEnd  multiplicity="(1 1)"
	 */
	protected LegSensorsVcnl4020 vcnl4020set;

	
	
public LegSensors(DeviceMetaData metaData)
{
	super(metaData);
	
	

	this.aquisators = LegSensorsDataAquisator.aquisators;
	
	
	this.vcnl4020set = new LegSensorsVcnl4020(LegSensorsProtocol.getVcnl4000Protocol(this.getId()));
	this.addComponentSet(this.vcnl4020set);

	this.ledSet = new LegSensorsLedSet(LegSensorsProtocol.getLedProtocol(this.getId()));
	this.addComponentSet(this.ledSet);
	
	
	this.protocol=new LegSensorsProtocol(this);

}







public void loadSetup()
{

	this.vcnl4020set.loadSettings();
		
}



public Vcnl4000Set getVcnl4000Set()
{
	return (this.vcnl4020set);
}






/*
@Override
public ArrayList<ComponentValue<?>> getInputValues()
{
	ArrayList<ComponentValue<?>> values = new ArrayList<ComponentValue<?>>();

	
	for (Mlx90614 sensor: this.mxl90614Set)
	{
		values.add(sensor.getAmbientValue());
		values.add(sensor.getObjectValue());
	}
	
	

	values.addAll(this.bmp085SensorSet.getValues());
	
	values.addAll(this.mxl90614Set.getValues());
	
	values.addAll(this.vcnl4000set.getValues());
	return(values);
}

*/




}
"""