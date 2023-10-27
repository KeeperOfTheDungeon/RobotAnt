import argparse




from RoboControl.Com.SerialConnection import SerialConnection
from ant import Ant
from AntView.AntView import AntView



def main(do_gui: bool, do_cli: bool):
    ant = Ant()
    yield ant
    if do_gui:
        ant_viewer = AntView(ant)
        # yield ant_viewer
    if do_cli:
        available_ports = SerialConnection.get_ports()
        port = SerialConnection.port if SerialConnection.port in available_ports else available_ports[0].name
        connection = ant._connection.set_port(port)
        ant.connect(connection)
        ant.run()


def parse_args():
    parser = argparse.ArgumentParser(description='GUI/CLI for the Ant robot from HsKa.')
    parser.add_argument('--gui', action=argparse.BooleanOptionalAction)
    parser.add_argument('--cli', action=argparse.BooleanOptionalAction)
    parser.set_defaults(gui=True, cli=False)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    resources = []
    try:
        resources += main(args.gui, args.cli) or []
    except KeyboardInterrupt:
        print('Interrupted ! (ctrl+c)')
    finally:
        print("Disconnecting: ", resources)
        for r in resources:
            try:
                r.disconnect()
            except Exception as e:
                print(f"Couldn't disconnect {r}: {e}")
    print("Shutting down!")
