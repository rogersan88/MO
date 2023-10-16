"""This module contains the class in charge of configuring the selenium driver"""
import os
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.ui import WebDriverWait
from utilities.config_manager import ConfigManager
from utilities.logging_config import Log
from selenium.webdriver.chrome.service import Service


class SetParameterDriver:
    """This class contains the methods that configure to use the driver"""

    @staticmethod
    def driver_configuration() -> webdriver:
        """
        Initial driver configuration
        :return webdriver
        """
        options = webdriver.ChromeOptions()

        if ConfigManager.get_value("headlessMode") == "Enabled":
            options.add_argument("--headless")
            options.add_experimental_option('excludeSwitches', ["enable-logging"])
        else:
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.add_experimental_option("prefs", {
                "download.default_directory": True, "download.directory_upgrade": True,
                "download.prompt_for_download": False, 'safebrowsing.enabled': False,
                'safebrowsing_for_trusted_sources_enabled': False

            })

        service = Service(executable_path=os.getcwd() + "\\drivers\\" + ConfigManager.get_value("pathDriver"))
        driver = webdriver.Chrome(service=service, options=options)
        driver.delete_all_cookies()
        driver.maximize_window()
        driver.implicitly_wait(ConfigManager.get_value("ExpectedWaitingTime"))
        Log().get_logger().info("The driver is successfully configured")

        return driver

    @staticmethod
    def set_waiting_time(driver) -> webdriver:
        """
        Configuration of the driver waits
        :param driver
        :return WebdriverWait
        """
        Log().get_logger().info("Timeout successfully configured")
        ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
        return  WebDriverWait(driver, timeout=ConfigManager.get_value("ExpectedWaitingTime"), poll_frequency=1, ignored_exceptions=ignore_list)

    @staticmethod
    def close_driver(driver):
        """
        Closes the driver after execution
        :param driver
        """
        driver.close()
        driver.quit()
        Log().get_logger().info("Driver successfully closed")
