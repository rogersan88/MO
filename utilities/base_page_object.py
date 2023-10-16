"""This module contains the class with the most common methods to interact with the pages"""
import time

from selenium.common.exceptions import (NoSuchElementException)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class PageObject:
    """This class contains the common methods to interact with a page"""

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.actions = ActionChains(self.driver)

    def do_click(self, locator: By) -> object:
        """
        Click on a page element
        :param locator
        """
        self.wait.until(EC.presence_of_all_elements_located(locator))
        self.wait.until(EC.visibility_of_element_located(locator))
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def hide(self, locator: By) -> object:
        """
        Wait for the locator to hide in the page
        :param locator
        """
        self.wait.until(EC.invisibility_of_element_located(locator))

    def do_double_click(self, locator: By):
        """
        Double click on a page element
        :param locator
        """
        self.wait.until(EC.element_to_be_clickable(locator))
        self.actions.double_click(self.driver.find_element(*locator)).perform()

    def do_send_keys(self, locator: By, text: str) -> object:
        """
        Sends keys to an input element on the page
        :param locator
        :param text
        """
        self.wait.until(EC.visibility_of_element_located(locator))
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(text)

    def do_send_keys_file(self, locator: By, text: str) -> object:
        """
        Sends keys to an input element on the page (File Explorer)
        :param locator
        :param text
        """

        self.driver.find_element(*locator).send_keys(text)

    def get_text(self, locator: By) -> str:
        """
        Gets the text of a page element
        :param locator
        """

        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def wait_element_to_be_clickable(self, locator: By) -> object:
        """
        Wait for a page element to be click
        :param locator:
        """
        self.wait.until(EC.element_to_be_clickable(locator))

    def wait_element(self, locator: By) -> object:
        """
        Waits for a page element to become visible
        :param locator:
        """
        self.wait.until(EC.visibility_of_element_located(locator))

    def function_control_enter(self):
        """Execute the CTRL + ENTER key combination"""
        self.actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).perform()

    def element_is_displayed(self, locator: By) -> bool:
        """
        Checks that an element is visible and returns a boolean
        :param locator
        :return bool
        """
        try:
            visible = self.driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            visible = False
        return visible

    def generate_or_download_ditsheet(self, locator_g, locator_d):
        """
        Generate or download a dig sheet
        :param locator_g,locator_d
        """
        if self.wait.until(EC.visibility_of_element_located(locator)):
            self.do_click(locator_g)
        else:
            self.do_click(locator_d)

    def get_css_attribute(self, locator: object, attribute: object) -> object:
        """
        Return the CSS attribute value of the page element
        """
        return self.wait.until(EC.visibility_of_element_located(locator)).value_of_css_property(attribute)

    def move_element(self, locator: By) -> object:
        self.actions.move_to_element(self.driver.find_element(*locator)).perform()
