from behave import *
from model.login import LoginPage
from utilities.config_manager import ConfigManager


@Given('The user enters the website')
def open_website(context):
    context.driver.get(ConfigManager.get_value('URL'))


@when('Enter username and password')
def enter_username_password(context):
    context.login = LoginPage(context.driver, context.wait)
    context.login.enter_user(ConfigManager.get_value('user'))
    context.login.enter_password(ConfigManager.get_value('password'))
    context.login.click_on_button_login()


@Then('The user should be logged in')
def check_loggin(context):
    """
  Validates that the user was able to log in to the page
  """
    assert context.login.get_label_welcome_user() == ConfigManager.get_value('welcome_user'), ('Error the message '
                                                                                               'received was: ') + str(
        context.login.get_label_welcome_user())

    context.login.click_on_button_log_out()
    assert context.login.get_label_title_test_login() == ConfigManager.get_value('test_login'), ('Error the message '
                                                                                                 'received was: ') + str(
        context.login.get_label_title_test_login())
