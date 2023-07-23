from RoboView.Robot.Device.Viewer.DeviceView import DeviceView
from RoboView.Robot.component.sensor.generic.distance.view.DistanceSensorDataView import DistanceSensorDataView
from RoboView.Robot.component.sensor.generic.lux.view.LuxSensorDataView import LuxSensorDataView


class HeadSensorsDataView(DeviceView):
    def __init__(self, device, window_bar):
        super().__init__("Head Sensors Data", device, window_bar)
        self.make_display(device)

    def make_display(self, device):
        vcln_4000_sensors = device.get_vcnl_4000_set()

        for sensor in vcln_4000_sensors:
            view = DistanceSensorDataView.create_view(
                self._display, sensor.get_distance_sensor(), self._settings_key)

            view = LuxSensorDataView.create_view(
                self._display, sensor.get_lux_sensor(), self._settings_key)


"""

private void makeDisplay(String robotName, HeadSensors hs) 
{

	this.setDevice(robotName, hs);
	
	for ( Mlx90614 sensor : hs.getMlx90614Set())
	{
		this.addComponent(TemperatureSensorDataView.createView(sensor.getAmbientSensor()));
		this.addComponent(TemperatureSensorDataView.createView(sensor.getObjectSensor()));
	}



	for ( Vcnl4000 sensor : hs.getVcnl4000Set())
	{
		this.addComponent(LuxSensorDataView.createView(sensor.getLuxSensor()));
		this.addComponent(DistanceSensorDataView.createView(sensor.getDistanceSensor()));
	}
	/*
	for ( m sensor : hs.getBmp085Set())
	{
		this.addComponent(TemperatureSensorDataView.createView(sensor.getTemperatureSensor()));
		this.addComponent(BarometricSensorDataView.createView(sensor.getBarometricSensor()));

	}
	*/
}
"""

"""
package de.hska.lat.ant.devices.headSensors;


import de.hska.lat.ant.metaData.AntDeviceId;
import de.hska.lat.robot.abstractRobot.AbstractRobot;

import de.hska.lat.robot.component.view.ComponentView;
import de.hska.lat.robot.component.view.MissingComponentView;

import de.hska.lat.robot.component.digitalDetector.DigitalDetector;
import de.hska.lat.robot.component.generic.distance.view.DistanceSensorDataView;
import de.hska.lat.robot.component.generic.lux.view.LuxSensorDataView;
import de.hska.lat.robot.component.generic.temperature.view.TemperatureSensorDataView;


import de.hska.lat.robot.component.temperatureSensor.mlx90614.Mlx90614;


import de.hska.lat.robot.component.sensor.vcnl4000.Vcnl4000;





import de.hska.lat.robot.device.viewer.DeviceView;

import de.hska.lat.robot.value.view.detector.DetectorValueView;




public class HeadSensorsDataView extends DeviceView
{



	
/**
	 * 
	 */
	private static final long serialVersionUID = 1840040237898819284L;


@Override
public boolean setRobot(AbstractRobot<?,?,?> robot)
{
	HeadSensors hs;
	
	hs=(HeadSensors)robot.getDeviceOnName(AntDeviceId.HEAD_SENSORS.getName());
	
			
	if (hs!=null)
	{
		this.makeDisplay(robot.getName(), hs);
		return(true);
	}
	else
	{
		this.makeErrorDisplay(HeadSensors.class.getName());
		return(false);
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
