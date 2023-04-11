import tkinter as tk

from AntView.Devices.LegSensors.LegSensorsControlView import LegSensorsControlView
from RoboView.Robot.Viewer.RobotSettings import RobotSettings

from AntView.Devices.LegSensors.LegSensorsDataView import LegSensorsDataView
from AntView.Devices.LegSensors.LegSensorsSetupView import LegSensorsSetupView
from AntView.Devices.headSensors.HeadSensorsDataView import HeadSensorsDataView
from AntView.Devices.legController.LegControllerControlView import LegControllersControlView
from AntView.Devices.legController.LegControllerDataView import LegControllersDataView
from AntView.Devices.legController.LegControllerSetupView import LegControllerSetupView

from RoboView.Robot.Device.generic.dataHub.view.DataHubDataView import DataHubDataView
from RoboView.Robot.Viewer.RobotViewer import RobotViewer
from RoboView.Gui.InternalWindow.WindowState import State
from ant import Ant


class AntView(RobotViewer):
    _robot: Ant

    def __init__(self, *args):
        super().__init__(*args)

        # FIXME why do these need to be saved separately
        self._main_data_hub_data = None
        self._head_sensors_data = None
        self._leg_sensors_data = None
        self._leg_controller_data = None

    def make_data_menu(self, menue_bar: tk.Menu) -> None:

        # FIXME menue is likely a typo
        menue = tk.Menu(menue_bar)
        menue.add_command(label="Data Hub",
                          command=self.show_data_hub_data)
        menue.add_command(label="Head Sensors",
                          command=self.show_head_sensors_data)
        menue.add_command(label="Leg Sensors",
                          command=self.show_leg_sensors_data)
        menue.add_command(label="Leg Controller",
                          command=self.show_leg_controller_data)
        menue_bar.add_cascade(label="Data View", menu=menue)

    def make_control_menu(self, menue_bar: tk.Menu) -> None:
        menue = tk.Menu(menue_bar)
        menue.add_command(label="Leg Sensors",
                          command=self.show_leg_sensors_control)
        menue.add_command(label="Leg Controller",
                          command=self.show_leg_controller_control)
        menue_bar.add_cascade(label="Control View", menu=menue)

    def make_setup_menu(self, menue_bar: tk.Menu) -> None:
        menue = tk.Menu(menue_bar)
        menue.add_command(label="Leg Sensors",
                          command=self.show_leg_sensors_setup)
        menue.add_command(label="Leg Controller",
                          command=self.show_leg_controller_setup)
        menue_bar.add_cascade(label="Setup View", menu=menue)

    # data view
    def show_data_hub_data(self):
        if (not RobotSettings.get_int("{}.state".format("DataHubDataView")) == State.INTERNAL.value
                and not RobotSettings.get_int("{}.state".format("DataHubDataView")) == State.EXTERNAL.value):
            print("show Data hub data")
            device = self._robot.get_data_hub()
            self._main_data_hub_data = DataHubDataView(device, self._window_bar)
            self._main_data_hub_data.draw()
        else:
            print("{} already open".format("DataHubDataView"))

    def show_head_sensors_data(self):
        if (not RobotSettings.get_int("{}.state".format("HeadSensorsDataView")) == State.INTERNAL.value
                and not RobotSettings.get_int("{}.state".format("HeadSensorsDataView")) == State.EXTERNAL.value):
            print("show head Sensors data")
            device = self._robot.get_head_sensors()
            self._head_sensors_data = HeadSensorsDataView(device, self._window_bar)
            self._head_sensors_data.draw()
        else:
            print("{} already open".format("HeadSensorsDataView"))

    # leg data
    def show_leg_sensors_data(self):
        if (not RobotSettings.get_int("{}.state".format("LegSensorsDataView")) == State.INTERNAL.value
                and not RobotSettings.get_int("{}.state".format("LegSensorsDataView")) == State.EXTERNAL.value):
            print("show leg Sensors data")
            device = self._robot.get_leg_sensors()
            self._leg_sensors_data = LegSensorsDataView(device, self._window_bar)
            self._leg_sensors_data.draw()
        else:
            print("{} already open".format("LegSensorsDataView"))

    def show_leg_controller_data(self):
        if (not RobotSettings.get_int("{}.state".format("LegControllersDataView")) == State.INTERNAL.value
                and not RobotSettings.get_int("{}.state".format("LegControllersDataView")) == State.EXTERNAL.value):
            print("show leg controller data")
            device = self._robot.get_leg_controller()
            self._leg_controller_data = LegControllersDataView(device, self._window_bar)
            self._leg_controller_data.draw()
        else:
            print("{} already open".format("LegControllersDataView"))

    # leg control
    def show_leg_sensors_control(self):
        if (not RobotSettings.get_int("{}.state".format("LegSensorsControlView")) == State.INTERNAL.value
                and not RobotSettings.get_int("{}.state".format("LegSensorsControlView")) == State.EXTERNAL.value):
            print("show leg sensors control")
            device = self._robot.get_leg_sensors()
            self._leg_controller_data = LegSensorsControlView(device, self._window_bar)
            self._leg_controller_data.draw()
        else:
            print("{} already open".format("LegSensorsControlView"))

    def show_leg_controller_control(self):
        if (not RobotSettings.get_int("{}.state".format("LegControllersControlView")) == State.INTERNAL.value
                and not RobotSettings.get_int("{}.state".format("LegControllersControlView")) == State.EXTERNAL.value):
            print("show leg controller control")
            device = self._robot.get_leg_controller()
            self._leg_controller_data = LegControllersControlView(device, self._window_bar)
            self._leg_controller_data.draw()
        else:
            print("{} already open".format("LegControllersControlView"))

    # setup View
    def show_leg_controller_setup(self):
        if (not RobotSettings.get_int("{}.state".format("LegControllerSetupView")) == State.INTERNAL.value
                and not RobotSettings.get_int("{}.state".format("LegControllerSetupView")) == State.EXTERNAL.value):
            print("show leg controller setup")
            device = self._robot.get_leg_controller()
            self._leg_controller_data = LegControllerSetupView(device, self._window_bar)
            self._leg_controller_data.draw()
        else:
            print("{} already open".format("LegControllerSetupView"))

    def show_leg_sensors_setup(self):
        if (not RobotSettings.get_int("{}.state".format("LegSensorsSetupView")) == State.INTERNAL.value
                and not RobotSettings.get_int("{}.state".format("LegSensorsSetupView")) == State.EXTERNAL.value):
            print("show leg Sensors setup (not implemented)")
            # device = self._robot.get_leg_sensors()
            # self._leg_sensors_data = LegSensorsSetupView(device, self._window_bar)
            # self._leg_sensors_data.draw()
        else:
            print("{} already open".format("LegSensorsSetupView"))


"""
package de.hska.lat.ant;


import java.awt.event.ActionEvent;

import javax.swing.JMenu;


import de.hska.lat.ant.behavior.view.AntBehaviorViewer;

import de.hska.lat.ant.control.movementControl.MovementControlView;
import de.hska.lat.ant.devices.headSensors.HeadSensorsControlView;
import de.hska.lat.ant.devices.headSensors.HeadSensorsDataView;
import de.hska.lat.ant.devices.headSensors.HeadSensorsSetupView;
import de.hska.lat.ant.devices.legController.AntLegControllerControlView;
import de.hska.lat.ant.devices.legController.AntLegControllerDataView;
import de.hska.lat.ant.devices.legController.AntLegControllerSetupView;
import de.hska.lat.ant.devices.legSensors.LegSensorsControlView;
import de.hska.lat.ant.devices.legSensors.LegSensorsDataView;
import de.hska.lat.ant.devices.legSensors.LegSensorsSetupView;
import de.hska.lat.ant.devices.pixyController.PixyControlView;
import de.hska.lat.ant.devices.pixyController.PixySensorsDataView;
import de.hska.lat.ant.devices.pixyController.PixySensorsSetupView;
import de.hska.lat.ant.devices.tailBoard.TailBoardControlView;
import de.hska.lat.ant.devices.tailBoard.TailBoardDataView;
import de.hska.lat.ant.devices.tailBoard.TailBoardSetupView;

import de.hska.lat.ant.map.AntMap;




import de.hska.lat.robot.Robot;
import de.hska.lat.robot.RobotSettings;

import de.hska.lat.robot.viewer.RobotViewer;







public class AntView extends RobotViewer
{




	/**
	 * 
	 */
	private static final long serialVersionUID = -266067081997282477L;
	protected final static String HEAD_SENSORS_TEXT =  "head sensors";
	protected final static String MOTION_CONTROLLER_TEXT = "motion controller";
	protected final static String LEG_CONTROLLER_TEXT = "leg controller";
	protected final static String LEG_SENSORS_TEXT = "leg sensors";
	protected final static String TAIL_BOARD_TEXT = "tail board";
	protected final static String PIXY_TEXT = "pixy board";
	
public AntView()
{
	super("Ant");
	

}

	
public AntView(Robot robot)
{
	super("Ant");
	

	
	this.setRobot(robot);
	
	this.toFront();
	this.setVisible(true);	

}
	
public void setRobot(Robot robot)
{
	super.setRobot(robot);
}	









protected JMenu makeDataMenu()
{

	JMenu	tmpMenu;
	
	tmpMenu=super.makeDataMenu();
	
	tmpMenu.add(this.addDataHubDataView());
	
	//tmpMenu.add(makeMenuItem(MOTION_CONTROLLER_STRING,CMD_SHOW_VIEW+MOTION_CONTROLLER_DATA_VIEW));
	tmpMenu.add(makeMenuItem(LEG_CONTROLLER_TEXT,CMD_SHOW_FRAME+this.addDisplay(AntLegControllerDataView.class.getName())));

	tmpMenu.add(makeMenuItem(HEAD_SENSORS_TEXT,CMD_SHOW_FRAME+this.addDisplay(HeadSensorsDataView.class.getName())));
	tmpMenu.add(makeMenuItem(TAIL_BOARD_TEXT,CMD_SHOW_FRAME+this.addDisplay(TailBoardDataView.class.getName())));
	
	tmpMenu.add(makeMenuItem(LEG_SENSORS_TEXT,CMD_SHOW_FRAME+this.addDisplay(LegSensorsDataView.class.getName())));
	
	tmpMenu.add(makeMenuItem(PIXY_TEXT,CMD_SHOW_FRAME+this.addDisplay(PixySensorsDataView.class.getName())));
	
	
	tmpMenu.add(makeMenuItem("map",CMD_SHOW_FRAME+this.addDisplay(AntMap.class.getName())));
	
	
	
	return(tmpMenu);
}




protected JMenu makeControlMenu()
{

	JMenu	tmpMenu;
	
	tmpMenu=super.makeControlMenu();
	tmpMenu.add(makeMenuItem(LEG_CONTROLLER_TEXT,CMD_SHOW_FRAME+this.addDisplay(AntLegControllerControlView.class.getName())));
	tmpMenu.add(makeMenuItem(MOTION_CONTROLLER_TEXT,CMD_SHOW_FRAME+this.addDisplay(MovementControlView.class.getName())));
	tmpMenu.add(makeMenuItem(HEAD_SENSORS_TEXT,CMD_SHOW_FRAME+this.addDisplay(HeadSensorsControlView.class.getName())));
	tmpMenu.add(makeMenuItem(TAIL_BOARD_TEXT,CMD_SHOW_FRAME+this.addDisplay(TailBoardControlView.class.getName())));
	tmpMenu.add(makeMenuItem(LEG_SENSORS_TEXT,CMD_SHOW_FRAME+this.addDisplay(LegSensorsControlView.class.getName())));

	tmpMenu.add(makeMenuItem(PIXY_TEXT,CMD_SHOW_FRAME+this.addDisplay(PixyControlView.class.getName())));
	
	
	return(tmpMenu);
}



protected JMenu makeSetupMenu()
{

	JMenu	tmpMenu;
	
	tmpMenu=super.makeSetupMenu();
	
	tmpMenu.add(makeMenuItem(LEG_CONTROLLER_TEXT,CMD_SHOW_FRAME+this.addDisplay(AntLegControllerSetupView.class.getName())));
	tmpMenu.add(makeMenuItem(HEAD_SENSORS_TEXT,CMD_SHOW_FRAME+this.addDisplay(HeadSensorsSetupView.class.getName())));
	tmpMenu.add(makeMenuItem(TAIL_BOARD_TEXT,CMD_SHOW_FRAME+this.addDisplay(TailBoardSetupView.class.getName())));

		
	tmpMenu.add(makeMenuItem(LEG_SENSORS_TEXT,CMD_SHOW_FRAME+this.addDisplay(LegSensorsSetupView.class.getName())));
	tmpMenu.add(makeMenuItem(PIXY_TEXT,CMD_SHOW_FRAME+this.addDisplay(PixySensorsSetupView.class.getName())));


	
	return(tmpMenu);
}

protected JMenu makeBehaviorMenu()
{
	JMenu	tmpMenu;
	
	tmpMenu = new JMenu(RobotViewer.MENUE_NAME_BEHAVIOR);
	tmpMenu.add(makeMenuItem(RobotViewer.MENUE_NAME_SHOW_BEHAVIOR,RobotViewer.CMD_SHOW_BEHAVIOR));

//BehaviorViewer
	//MENUE_NAME_SHOW_BEHAVIOR
	return(tmpMenu);
}





@Override
public void actionPerformed(ActionEvent actionEvent)
{
	String cmd;
	
	cmd=actionEvent.getActionCommand();
	

	if (cmd.equals(CMD_SHOW_BEHAVIOR))
	{
		RobotSettings settings = new RobotSettings();
		settings.setFileName("config/behaviordesktop.cfg");
		settings.loadSettings();
		new AntBehaviorViewer(this.robot.getBehavior(), settings);
	}
	else
	{
		super.actionPerformed(actionEvent);
		
	}
	

}



}

"""
