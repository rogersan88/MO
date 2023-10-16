from utilities.driver_config import SetParameterDriver
from utilities.logging_config import Log


def before_feature(context, feature):
    """Config driver and wait"""
    Log().get_logger().info("---------------- Test Starts ----------------")
    Log().get_logger().info(str(feature))
    context.driver = SetParameterDriver.driver_configuration()
    context.wait = SetParameterDriver.set_waiting_time(context.driver)


def after_feature(context, feature):
    """Close the driver"""
    SetParameterDriver.close_driver(context.driver)
    Log().get_logger().info("---------------- Test Ends ----------------")
