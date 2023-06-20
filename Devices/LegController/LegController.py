from Devices.LegController.LegControllerCurrentSensors import LegControllerCurrentSensors
from Devices.LegController.LegControllerProtocol import LegControllerProtocol
from Devices.LegController.LegControllerServoSet import LegControllerServos
from RoboControl.Robot.Device.RobotDevice import RobotDevice

from RoboControl.Robot.Device.RobotDevice import RobotDevice


class LegController(RobotDevice):

    def __init__(self, component_config):
        super().__init__(component_config)

    def build(self):
        self._protocol = LegControllerProtocol(self)

        protocol = self._protocol.get_servo_protocol()
        self._servo_set = LegControllerServos(protocol)
        self.add_components(self._servo_set)

        protocol = self._protocol.get_current_protocol()
        self._current_sensor_set = LegControllerCurrentSensors(protocol)
        self.add_components(self._current_sensor_set)

        self.build_protocol()

    def build_protocol(self):
        super().build_protocol()

        self._remote_command_processor_list.extend(self._servo_set.get_command_processors())
        self._remote_command_processor_list.extend(self._current_sensor_set.get_command_processors())

        self._remote_message_processor_list.extend(self._servo_set.get_message_processors())
        self._remote_message_processor_list.extend(self._current_sensor_set.get_message_processors())

        self._remote_stream_processor_list.extend(self._servo_set.get_stream_processors())
        self._remote_stream_processor_list.extend(self._current_sensor_set.get_stream_processors())

    def get_servo_set(self):
        return self._servo_set

    def get_current_sensors(self):
        return self._current_sensor_set

    def get_data_aquisators(self):
        aquisators = super().get_data_aquisators()
        aquisators.extend(["servo Positionse",
                           "Servo Destinations",
                           "Servo Status",
                           "current consumption",
                           "current max consumption",
                           "current Total consumption",
                           "servo raw analogue values",
                           "temperatures"])
        return aquisators


"""package de.hska.lat.ant_IIIb.devices.legController;



import de.hska.lat.ant_IIIb.component.motion.AntMotionController;
import de.hska.lat.ant_IIIb.devices.legController.components.LegControllerCurrentSensors;
import de.hska.lat.ant_IIIb.devices.legController.components.LegControllerLm75;
import de.hska.lat.ant_IIIb.devices.legController.components.LegControllerServos;
import de.hska.lat.ant_IIIb.metaData.AntComponents;
import de.hska.lat.robot.component.actor.servo.Servo;
import de.hska.lat.robot.component.actor.servo.ServoSet;
import de.hska.lat.robot.component.currentSensor.CurrentSensor;
import de.hska.lat.robot.component.sensor.lm75.Lm75;
import de.hska.lat.robot.device.DeviceEventNotifier;
import de.hska.lat.robot.device.DeviceMetaData;
import de.hska.lat.robot.device.RobotDevice;



public class LegController extends RobotDevice <DeviceEventNotifier, LegControllerProtocol>
{

    /**
     * @uml.property  name="servos"
     */
    
    protected LegControllerCurrentSensors currentSensors;
    
    protected LegControllerServos servos;	
    
    protected LegControllerLm75 temperatureSensors;
    
    /**
     * @uml.property  name="motionController"
     * @uml.associationEnd  multiplicity="(1 1)"
     */
    protected AntMotionController motionController;
    
public LegController(DeviceMetaData metaData)
{
    super(metaData); 
    aquisators= LegControllerDataAquisator.aquisators;

    this.servos  = new LegControllerServos(LegControllerProtocol.getServoProtocol(this.getId()));
    this.addComponentSet(this.servos);	
 
    
    this.currentSensors  = new LegControllerCurrentSensors(LegControllerProtocol.getCurrentProtocol(this.getId()));
    this.addComponentSet(this.currentSensors);	
 
    
    this.temperatureSensors  = new LegControllerLm75(LegControllerProtocol.getTemperatureProtocol(this.getId()));
    this.addComponentSet(this.temperatureSensors);	
 
    
    this.motionController  = new AntMotionController(AntComponents.MOTION_CONTROLLER.getMetaData(), LegControllerProtocol.getMotionProtocol(this.getId()),this); 
    this.componentList.add(this.motionController);
    
    
    
    
    
    this.protocol=new LegControllerProtocol(this);

}





/**
 * @return
 * @uml.property  name="servos"
 */
public ServoSet getServos()
{
    return (this.servos);
}


public LegControllerCurrentSensors getCurrentSensors()
{
    return(currentSensors);
}


public void loadSetup()
{
    for (Servo servo : this.servos)
    {
        servo.remote_loadDefaults();
        servo.remote_getSettings();
        servo.remote_getServoSpeed();
        servo.remote_getServoStatus();
    
    }
    
    for (CurrentSensor current :this.currentSensors)
    {
        current.remote_getSettings();
    }

    
    for (Lm75 lm75 :this.temperatureSensors)
    {
        lm75.remote_getSettings();
    }
    
}





public LegControllerLm75 getTemperatureSensors()
{
    return (this.temperatureSensors);
}




}


"""
