import customtkinter as ctk

from Devices.AntDeviceConfig import AntDeviceConfig
from Devices.LegSensors.LegSensors import LegSensors
from RoboControl.Robot.AbstractRobot.AbstractRobot import AbstractRobot
from RoboView.Robot.Device.Viewer.DeviceView import DeviceView
from RoboView.Robot.Viewer.WindowBar import WindowBar
from RoboView.Robot.component.sensor.generic.distance.view.DistanceSensorDataView import DistanceSensorDataView
from RoboView.Robot.component.sensor.generic.lux.view.LuxSensorDataView import LuxSensorDataView
from RoboView.Robot.component.view.ComponentView import ComponentView
from RoboView.Robot.component.view.MissingComponentView import MissingComponentView


class LegSensorsDataView(DeviceView):
    FRAME_NAME: str = "Leg Sensors Data"

    def __init__(self, root: ctk.CTkFrame, device: LegSensors, window_bar: WindowBar):
        super().__init__(root, device, window_bar)
        self.make_display(device)

    def make_display(self, device):
        vcln_4000_sensors = device.get_vcnl_4000_set()

        for sensor in vcln_4000_sensors:
            view = DistanceSensorDataView.create_view(
                self._display, sensor.get_distance_sensor(), self._settings_key)

            view = LuxSensorDataView.create_view(
                self._display, sensor.get_lux_sensor(), self._settings_key)

    def set_robot(self, robot):
        pass


"""package de.hska.lat.ant.devices.legSensors;


import de.hska.lat.ant.metaData.AntDeviceId;
import de.hska.lat.robot.abstractRobot.AbstractRobot;
import de.hska.lat.robot.component.view.ComponentView;
import de.hska.lat.robot.component.view.MissingComponentView;
import de.hska.lat.robot.component.actor.led.Led;
import de.hska.lat.robot.component.actor.led.view.LedDataView;
import de.hska.lat.robot.component.digitalDetector.DigitalDetector;
import de.hska.lat.robot.component.generic.distance.view.DistanceSensorDataView;
import de.hska.lat.robot.component.generic.lux.view.LuxSensorDataView;
import de.hska.lat.robot.component.sensor.vcnl4000.Vcnl4000;





import de.hska.lat.robot.device.viewer.DeviceView;

import de.hska.lat.robot.value.view.detector.DetectorValueView;




public class LegSensorsDataView extends DeviceView
{



	
/**
	 * 
	 */
	private static final long serialVersionUID = 1840040237898819284L;


@Override
public boolean setRobot(AbstractRobot<?,?,?> robot)
{
	LegSensors ls;
	
	ls=(LegSensors)robot.getDeviceOnName(AntDeviceId.LEG_SENSORS.getName());
	
			
	if (ls!=null)
	{
		this.makeDisplay(robot.getName(), ls);
		return(true);
	}
	else
	{
		this.makeErrorDisplay(LegSensors.class.getName());
		return(false);
	}
}



private void makeDisplay(String robotName, LegSensors ls) 
{

	this.setDevice(robotName, ls);
	



	for ( Vcnl4000 sensor : ls.getVcnl4000Set())
	{
		this.addComponent(LuxSensorDataView.createView(sensor.getLuxSensor()));
		this.addComponent(DistanceSensorDataView.createView(sensor.getDistanceSensor()));
	}
	
	
	for ( Led led : ls.getLedSet())
	{
		this.addComponent(LedDataView.createView(led));
	}
	
	
}




public ComponentView addDetector(DigitalDetector detector)
{
	if (detector!=null)
	{
		return(new DetectorValueView(detector.getValue(),false));
	}
	else
	{
		return(new MissingComponentView(DigitalDetector.class.getName()));
	}
}





}
"""
