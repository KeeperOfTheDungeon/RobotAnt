from Devices.HeadSensors.HeadSensorsProtocol import HeadSensorsProtocol
from Devices.HeadSensors.HeadSensorsVcnl4020Set import HeadSensorsVcnl4020Set
from RoboControl.Robot.Device.RobotDevice import RobotDevice


class HeadSensors(RobotDevice):

    def __init__(self, component_config):
        super().__init__(component_config)

    def build(self):
        self._protocol = HeadSensorsProtocol(self)

        protocol = self._protocol.get_vcnl4000_protocol()
        self._vcnl_4020_set = HeadSensorsVcnl4020Set(protocol)
        self.add_components(self._vcnl_4020_set)

        self.build_protocol()

    def build_protocol(self):
        super().build_protocol()
        self._remote_command_processor_list.extend(self._vcnl_4020_set.get_command_processors())
        self._remote_message_processor_list.extend(self._vcnl_4020_set.get_message_processors())
        self._remote_stream_processor_list.extend(self._vcnl_4020_set.get_stream_processors())

    def get_data_aquisators(self):
        aquisators = super().get_data_aquisators()
        aquisators.extend(["Mxl90614 ambient temperature", "Mxl90614 object temperature", "lux", "distance"])
        return aquisators

    def get_vcnl_4000_set(self):
        return self._vcnl_4020_set

    def _load_setup(self):
        self._vcnl_4020_set.load_settings()


"""package de.hska.lat.ant_IIIb.devices.headSensors;


HeadSensorsVcnl4020






import de.hska.lat.ant_IIIb.devices.headSensors.components.HeadMlx90614Set;
import de.hska.lat.ant_IIIb.devices.headSensors.components.HeadSensorsVcnl4000Set;
import de.hska.lat.robot.component.temperatureSensor.mlx90614.Mlx90614Set;


import de.hska.lat.robot.component.actor.servo.analogServo.AnalogServoServoSet;
import de.hska.lat.robot.component.sensor.bmp085.Bmp085Set;


import de.hska.lat.robot.device.DeviceEventNotifier;
import de.hska.lat.robot.device.DeviceMetaData;
import de.hska.lat.robot.device.RobotDevice;





public class HeadSensors extends RobotDevice<DeviceEventNotifier, HeadSensorsProtocol >
{
    
    /**
     * @uml.property  name="servos"
     */
    protected AnalogServoServoSet	servos;
    
    /**
     * @uml.property  name="vcnl4000set"
     * @uml.associationEnd  multiplicity="(1 1)"
     */
    protected HeadSensorsVcnl4000Set vcnl4000set;
    
    /**
     * @uml.property  name="mxl90614Set"
     */
    protected HeadMlx90614Set mxl90614Set;
    
    /**
     * @uml.property  name="bmp085SensorSet"
     * @uml.associationEnd  multiplicity="(1 1)"
     */
    protected Bmp085Set bmp085SensorSet;
    
    
    
public HeadSensors(DeviceMetaData metaData)
{
    super(metaData);
    
    

    this.aquisators = HeadSensorsDataAquisator.aquisators;
    
//	this.addBmp085Sensors(metaData);

    
    this.mxl90614Set = new HeadMlx90614Set(HeadSensorsProtocol.getMlx90614Protocol(this.getId()));
    this.addComponentSet(this.mxl90614Set );
    
    this.vcnl4000set = new HeadSensorsVcnl4000Set(HeadSensorsProtocol.getVcnl4000Protocol(this.getId()));
    this.addComponentSet(this.vcnl4000set );
    
    
    
    this.protocol=new HeadSensorsProtocol(this);

}






/*
protected void addBmp085Sensors(HeadSensorsMetaData metaData)
{
    
    this.bmp085SensorSet = new Bmp085Set(metaData.getBmp085data(),HeadSensorsProtocol.getBmp085Protocol(this.getId()));
    this.addComponentSet(this.bmp085SensorSet);
}

*/


public void loadSetup()
{
    
    
    this.mxl90614Set.loadSettings();
    this.vcnl4000set.loadSettings();
//	this.bmp085SensorSet.loadSettings();
    
    
}

public Mlx90614Set getMlx90614Set()
{
    return(this.mxl90614Set);
    
}



public HeadSensorsVcnl4000Set getVcnl4000Set()
{
    return (this.vcnl4000set);
}



public Bmp085Set getBmp085Set()
{
    return (this.bmp085SensorSet);
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

/**
 * @return
 * @uml.property  name="servos"
 */
public AnalogServoServoSet getServos()
{
    return (this.servos);
}


}
"""
