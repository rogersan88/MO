"""This module contains the class in charge of configuring the logs"""
import logging
import os

from pathlib import Path
from utilities.config_manager import ConfigManager


class Singleton(type):
    """This class is in charge of implementing the singleton pattern"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """This method is in charge of maintaining a single installation"""
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Log(metaclass=Singleton):
    """In this class the project log is configured."""

    logger = None
    path_log = ConfigManager.get_value("pathLogs")

    if Path(path_log).exists():
        pass
    else:
        os.mkdir(path_log)

    def __init__(self):
        self.logger = logging.getLogger()
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%d/%m/%Y %H:%M:%S %p")
        file_handler = logging.FileHandler(os.path.join("", self.path_log, "Automation.log"))
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def get_logger(self):
        """
        This method writes to the .log file
        :return logger
        """
        return self.logger
