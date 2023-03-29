from Config import AntComponents
from RoboControl.Robot.Component.Sensor.vcnl4000.Vcnl4000 import Vcnl4000
from RoboControl.Robot.Component.Sensor.vcnl4000.Vcnl4000Set import Vcnl4000Set


class LegSensorsVcnl4000(Vcnl4000Set):

	def __init__(self, protocol):

		AntComponents.FRONT_LEFT_LEG_VCNL4020["protocol"] = protocol
		AntComponents.FRONT_RIGHT_LEG_VCNL4020["protocol"] = protocol
		AntComponents.CENTER_LEFT_LEG_VCNL4020["protocol"] = protocol
		AntComponents.CENTER_RIGHT_LEG_VCNL4020["protocol"] = protocol
		AntComponents.BACK_LEFT_LEG_VCNL4020["protocol"] = protocol
		AntComponents.BACK_RIGHT_LEG_VCNL4020["protocol"] = protocol

		sensor_list = [ AntComponents.FRONT_LEFT_LEG_VCNL4020,
						AntComponents.FRONT_RIGHT_LEG_VCNL4020,
						AntComponents.CENTER_LEFT_LEG_VCNL4020,
						AntComponents.CENTER_RIGHT_LEG_VCNL4020,
						AntComponents.BACK_LEFT_LEG_VCNL4020,
						AntComponents.BACK_RIGHT_LEG_VCNL4020]
		
		super().__init__(sensor_list, protocol)

