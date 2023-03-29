from RoboView.Robot.Device.Viewer.DeviceView import DeviceView
from RoboView.Robot.component.actor.servo.view.ServoSetupView import ServoSetupView

class LegControllerSetupView(DeviceView):
	def __init__(self, device, window_bar) :
		super().__init__( "Leg Controller Setup", device, window_bar)
		self.make_display(device)
		

	def make_display(self, device):

		servos = device.get_servo_set()
		for servo in servos:
			print("servo")
			ServoSetupView.create_view(self._display , servo, self._settings_key)


"""package de.hska.lat.ant.devices.legController;

import de.hska.lat.ant.metaData.AntDeviceId;
import de.hska.lat.robot.abstractRobot.AbstractRobot;

import de.hska.lat.robot.component.servo.view.ServoSetupView;
import de.hska.lat.robot.component.actor.servo.Servo;
import de.hska.lat.robot.component.actor.servo.ServoSet;
import de.hska.lat.robot.component.currentSensor.CurrentSensor;
import de.hska.lat.robot.component.currentSensor.CurrentSensorSet;
import de.hska.lat.robot.component.currentSensor.CurrentSetupView;
import de.hska.lat.robot.device.viewer.DeviceView;


public class AntLegControllerSetupView extends DeviceView
{



/**
	 * 
	 */
	private static final long serialVersionUID = -5337372269809597680L;

@Override
public boolean setRobot(AbstractRobot<?,?,?> robot)
{
	LegController legController;
	
	legController=(LegController)robot.getDeviceOnId(AntDeviceId.LEG_CONTROLLER.getId());
	
			
	if (legController!=null)
	{
		this.makeDisplay(robot.getName(), legController);
		return(true);
	}
	else
	{
		makeErrorDisplay(LegController.class.getName());
		return(false);
	}
}
	


public void makeDisplay(String robotName, LegController motionController)
{
	
	this.setDevice(robotName, motionController);
	
	

	this.addServos(motionController.getServos());
	this.addCurrents(motionController.getCurrentSensors());
	
}



protected void addServos(ServoSet servos)
{

	for (Servo servo : servos)
	{
		this.addComponent(ServoSetupView.createView(servo));
	}
}


protected void addCurrents(CurrentSensorSet currents)
{

	for (CurrentSensor current : currents)
	{
		this.addComponent(CurrentSetupView.createView(current));
	}
}

}
"""