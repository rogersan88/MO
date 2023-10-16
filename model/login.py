from selenium.webdriver.common.by import By

from utilities.base_page_object import PageObject
from utilities.logging_config import Log


class LoginPage(PageObject):
    def __init__(self, driver, wait):
        PageObject.__init__(self, driver, wait)
        self.log = Log().get_logger()

    INPUT_USER_NAME = (By.XPATH, "//*[@id='username']")
    INPUT_USER_PASSWORD = (By.XPATH, "//*[@id='password']")
    BUTTON_LOGIN = (By.XPATH, "//*[@id='submit']")
    WELCOME_USER = (By.XPATH, "//*[@id='loop-container']//strong")
    BUTTON_LOG_OUT = (By.XPATH, "//*[@class='wp-block-button__link has-text-color has-background "
                                "has-very-dark-gray-background-color']")
    TITLE_TEST_LOGIN = (By.XPATH, "//*[@id='login']/h2")

    def enter_user(self, username):
        """
        Enter the user to log in to the page
        """
        self.do_send_keys(self.INPUT_USER_NAME, username)
        self.log.info('Enter user successful')

    def enter_password(self, password):
        """
               Enter the password to log in to the page
               """
        self.do_send_keys(self.INPUT_USER_PASSWORD, password)
        self.log.info('Enter password successful')

    def click_on_button_login(self):
        """
        Click on the LOGIN button to log in the page
        """
        self.do_click(self.BUTTON_LOGIN)
        self.log.info('Click on button Login successful')

    def get_label_welcome_user(self):
        """
        get the text of the label corresponding to welcome (user)
        """
        self.log.info(self.get_text(self.WELCOME_USER))
        return self.get_text(self.WELCOME_USER)

    def click_on_button_log_out(self):
        """
        Click on the logout button  in the page
        """
        self.do_click(self.BUTTON_LOG_OUT)
        self.log.info('Click on button Log out successful')

    def get_label_title_test_login(self):
        """
        get the text of the label corresponding to test login
        """
        self.log.info(self.get_text(self.TITLE_TEST_LOGIN))
        return self.get_text(self.TITLE_TEST_LOGIN)