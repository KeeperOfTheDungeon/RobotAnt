import sys
import logging
import datetime

from settings import LOGS_LEVEL, PRETTY_MODE, SAVE_LOGS
from context import LOGS_PATH

SHOW_MODULE = False
ROOT_MODULE = '__main__'

logging.basicConfig(level=LOGS_LEVEL)


class Colors:
    GRAY = '\033[0;37m'
    RESET = '\033[0m'


def get_stdout_handler() -> logging.StreamHandler:
    try:
        if not PRETTY_MODE:
            raise ValueError("Pretty mode is disabled !")
        from rich.logging import RichHandler, Console
        handler = RichHandler(
            rich_tracebacks=True,
            console=Console(),
            log_time_format="[%X]"
        )
        formatter = logging.Formatter("%(message)s")
    except (ModuleNotFoundError, ValueError):
        handler = logging.StreamHandler(sys.stdout)
        if SHOW_MODULE:
            prefix = ("\t @" + Colors.GRAY + "%(name)s :" + Colors.RESET + "\n[%(levelname)s]")
        else:
            prefix = "[%(levelname)7s]"
        formatter = logging.Formatter(prefix + ' %(message)s')
    handler.setLevel(LOGS_LEVEL)
    handler.setFormatter(formatter)
    return handler


def get_file_handler() -> logging.FileHandler:
    now = datetime.datetime.now()
    date_str = now.strftime("%Y%m%d")
    datetime_str = now.strftime("%Y%m%d_%H%M%S")
    log_file = LOGS_PATH.joinpath(date_str).joinpath(datetime_str + ".log")
    log_file.parent.mkdir(parents=True, exist_ok=True)
    handler = logging.FileHandler(log_file)
    handler.setLevel(LOGS_LEVEL)
    formatter = logging.Formatter('%(asctime)s @ %(name)s : [%(levelname)s] %(message)s')
    handler.setFormatter(formatter)
    return handler


# noinspection PyPep8Naming
def getMainLogger() -> logging.Logger:
    logger = logging.getLogger(ROOT_MODULE)
    logger.propagate = False
    logger.addHandler(get_stdout_handler())
    if SAVE_LOGS:
        file_handler = get_file_handler()
        logger.debug("Persisting logs to : " + str(file_handler.baseFilename))
        logger.addHandler(file_handler)
    else:
        logger.debug("Not persisting logs as the SAVE_LOGS flag is disabled.")
    return logger


# noinspection PyPep8Naming
def getLogger(name: str = None) -> logging.Logger:
    return logging.getLogger(f'{ROOT_MODULE}.{name}' if name else ROOT_MODULE)
