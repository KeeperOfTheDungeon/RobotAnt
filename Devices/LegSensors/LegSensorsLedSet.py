from Config import AntConfig
from RoboControl.Robot.Component.Actor.Led import LedSet




class LegSensorsLedSet(LedSet):

    def __init__(self, protocol):
        AntConfig.FRONT_LEFT_LEG_LED["protocol"] = protocol
        AntConfig.FRONT_RIGHT_LEG_LED["protocol"] = protocol
        AntConfig.CENTER_LEFT_LEG_LED["protocol"] = protocol
        AntConfig.CENTER_RIGHT_LEG_LED["protocol"] = protocol
        AntConfig.BACK_LEFT_LEG_LED["protocol"] = protocol
        AntConfig.BACK_RIGHT_LEG_LED["protocol"] = protocol

        actor_list = [
            AntConfig.FRONT_LEFT_LEG_LED,
            AntConfig.FRONT_RIGHT_LEG_LED,
            AntConfig.CENTER_LEFT_LEG_LED,
            AntConfig.CENTER_RIGHT_LEG_LED,
            AntConfig.BACK_LEFT_LEG_LED,
            AntConfig.BACK_RIGHT_LEG_LED
        ]

        super().__init__(actor_list, protocol)


