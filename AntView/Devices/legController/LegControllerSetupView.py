import customtkinter as ctk

from Devices.AntDeviceConfig import AntDeviceConfig
from Devices.LegController.LegController import LegController
from RoboControl.Robot.AbstractRobot.AbstractRobot import AbstractRobot
from RoboControl.Robot.Component.Actor.servo.ServoSet import ServoSet
from RoboControl.Robot.Component.generic.currentSensor.CurrentSensorSet import CurrentSensorSet
from RoboView.Robot.Device.Viewer.DeviceView import DeviceView
from RoboView.Robot.Viewer.WindowBar import WindowBar
from RoboView.Robot.component.actor.servo.view.ServoDataView import ServoDataView
from RoboView.Robot.component.actor.servo.view.ServoSetupView import ServoSetupView
from RoboView.Robot.component.sensor.generic.currentSensor.CurrentSensorDataView import CurrentSensorDataView


class LegControllerSetupView(DeviceView):
    FRAME_NAME: str = "Leg Controller Setup"

    def __init__(self, root: ctk.CTkFrame, device: LegController, window_bar: WindowBar):
        super().__init__(root, device, window_bar)
        self.make_display(device)

    def make_display(self, device):
        servos = device.get_servo_set()
        for servo in servos:
            print("servo")
            ServoSetupView.create_view(self._display, servo, self._settings_key)


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
