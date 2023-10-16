"""This module contains the class in charge of reading the properties file"""
import configparser
import os

config = configparser.RawConfigParser()
config.read("properties.ini")


class ConfigManager:
    """This class contains the methods for reading the file properties"""
    @staticmethod
    def get_value(property_name: str) -> str:
        """
        Gets the data from the properties file
        :param property_name
        :return str
        """

        return config.get('common-info', property_name) \
            if os.environ.get(property_name, default=None) is None else None
