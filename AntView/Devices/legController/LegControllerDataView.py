import customtkinter as ctk

from Devices.AntDeviceConfig import AntDeviceConfig
from Devices.LegController.LegController import LegController
from RoboControl.Robot.AbstractRobot.AbstractRobot import AbstractRobot
from RoboView.Robot.Device.Viewer.DeviceView import DeviceView
from RoboView.Robot.Viewer.WindowBar import WindowBar
from RoboView.Robot.component.sensor.generic.currentSensor.CurrentSensorDataView import CurrentSensorDataView
from RoboView.Robot.component.actor.servo.view.ServoDataView import ServoDataView


class LegControllersDataView(DeviceView):  # AntLegControllerDataView extends MotionControllerDataView
    FRAME_NAME: str = "Leg Controller Data"

    def __init__(self, root: ctk.CTkFrame, device: LegController, window_bar: WindowBar):
        super().__init__(root, device, window_bar)
        self.make_display(device)

    def make_display(self, device):

        servos = device.get_servo_set()
        for servo in servos:
            view = ServoDataView.create_view(
                self._display, servo, self._settings_key)

        current_sensors = device.get_current_sensors()
        for sensor in current_sensors:
            view = CurrentSensorDataView.create_view(
                self._display, sensor, self._settings_key)

    # for sensor in vcln_4000_sensors:
    # view = DistanceSensorDataView.create_view(self._display , sensor.get_distance_sensor())
    # if view is not None:
    # view._frame.place(x = 50, y = 50 ,width = 50, height = 50)

    # view = LuxSensorDataView.create_view(self._display , sensor.get_lux_sensor())
    # view._frame.place(x = 150, y = 50 ,width = 50, height = 50)


"""package de.hska.lat.ant.devices.legController;

import de.hska.lat.ant.metaData.AntDeviceId;
import de.hska.lat.robot.abstractRobot.AbstractRobot;


import de.hska.lat.robot.component.servo.view.ServoDataView;
import de.hska.lat.robot.component.actor.servo.Servo;
import de.hska.lat.robot.component.actor.servo.ServoSet;
import de.hska.lat.robot.component.currentSensor.CurrentSensor;
import de.hska.lat.robot.component.currentSensor.CurrentSensorSet;
import de.hska.lat.robot.device.generic.motionController.MotionControllerDataView;
import de.hska.lat.robot.value.view.current.CurrentSensorDataView;


public class AntLegControllerDataView extends MotionControllerDataView
{



/**
	 * 
	 */
	private static final long serialVersionUID = -5337372269809597680L;

@Override
public boolean setRobot(AbstractRobot<?,?,?> asai)
{
	LegController legController;
	
	legController=(LegController)asai.getDeviceOnId(AntDeviceId.LEG_CONTROLLER.getId());
			
	if (legController!=null)
	{
		this.makeDisplay(asai.getName(), legController);
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
		this.addComponent(new ServoDataView(servo));
	}
}




protected void addCurrents(CurrentSensorSet currents)
{

	for (CurrentSensor current : currents)
	{
		this.addComponent(CurrentSensorDataView.createView(current));
	}
}



}
"""
