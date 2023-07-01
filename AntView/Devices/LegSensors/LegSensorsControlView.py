import customtkinter as ctk

from Devices.LegSensors.LegSensors import LegSensors
from RoboView.Robot.Device.Viewer.DeviceView import DeviceView
from RoboView.Robot.Viewer.WindowBar import WindowBar
from RoboView.Robot.component.actor.led.view.LedControlView import LedControlView


class LegSensorsControlView(DeviceView):
    FRAME_NAME: str = "Leg Sensors Control"

    def __init__(self, root: ctk.CTkFrame, device: LegSensors, window_bar: WindowBar):
        super().__init__(root, device, window_bar)
        self.make_display(device)

    def make_display(self, device):
        leds = device.get_led_set()
        for led in leds:
            view = LedControlView.create_view(self._display, led, self._settings_key)
        # if view is not None:
        # view._frame.place(x = 50, y = 50)


"""package de.hska.lat.ant.devices.legSensors;


import de.hska.lat.ant.metaData.AntDeviceId;
import de.hska.lat.robot.abstractRobot.AbstractRobot;
import de.hska.lat.robot.component.view.ComponentView;
import de.hska.lat.robot.component.view.MissingComponentView;
import de.hska.lat.robot.component.actor.led.Led;
import de.hska.lat.robot.component.actor.led.view.LedControlView;
import de.hska.lat.robot.component.digitalDetector.DigitalDetector;





import de.hska.lat.robot.device.viewer.DeviceView;

import de.hska.lat.robot.value.view.detector.DetectorValueView;




public class LegSensorsControlView extends DeviceView
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
	


	for ( Led led : ls.getLedSet())
	{
		this.addComponent(LedControlView.createView(led));
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





}"""
