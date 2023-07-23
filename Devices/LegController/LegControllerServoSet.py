from Config import AntComponents
from RoboControl.Robot.Component.Actor.servo.ServoSet import ServoSet


class LegControllerServos(ServoSet):
    def __init__(self, protocol):
        AntComponents.LEG_CONTROLLER_LEFT_SERVO["protocol"] = protocol
        AntComponents.LEG_CONTROLLER_CENTER_SERVO["protocol"] = protocol
        AntComponents.LEG_CONTROLLER_RIGHT_SERVO["protocol"] = protocol
        AntComponents.LEG_CONTROLLER_HEAD_SERVO["protocol"] = protocol

        sensor_list = [
            AntComponents.LEG_CONTROLLER_LEFT_SERVO,
            AntComponents.LEG_CONTROLLER_CENTER_SERVO,
            AntComponents.LEG_CONTROLLER_RIGHT_SERVO,
            AntComponents.LEG_CONTROLLER_HEAD_SERVO
        ]

        super().__init__(sensor_list, protocol)


"""
package de.hska.lat.ant_IIIb.devices.legController.components



import de.hska.lat.ant_IIIb.metaData.AntComponents;
import de.hska.lat.robot.component.actor.servo.ServoSet;
import de.hska.lat.robot.component.actor.servo.forceFeedback.ForceFeedbackServo;
import de.hska.lat.robot.component.actor.servo.forceFeedback.protocol.ForceFeedbackServoProtocol;



public class LegControllerServos extends ServoSet
{

    /**
     * 
     */
    private static final long serialVersionUID = -1455037511364580876L;

    public LegControllerServos(ForceFeedbackServoProtocol protocol)
    {


        this.add(new ForceFeedbackServo(AntComponents.LEFT_SERVO.getMetaData(), protocol));
        this.add(new ForceFeedbackServo(AntComponents.CENTER_SERVO.getMetaData(), protocol));
        this.add(new ForceFeedbackServo(AntComponents.RIGHT_SERVO.getMetaData(), protocol));
        this.add(new ForceFeedbackServo(AntComponents.HEAD_SERVO.getMetaData(), protocol));
    

    }

}
"""
