import yaml
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selenium.webdriver.support import expected_conditions as EC
import os
def get_driver():
    # Load configuration from config.yaml
    with open("config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)

    platform = config.get("platform", "android").lower()
    lt_options = {}

    # Set LambdaTest options based on config.yaml
    lt_options["deviceName"] = config.get("deviceName", "Galaxy.*" if platform == "android" else "iPhone.*")
    lt_options["platformName"] = platform.capitalize()
    lt_options["platformVersion"] = config.get("platformVersion", "10" if platform == "android" else "14")
    lt_options["build"] = config.get("build_name", "today Demo")
    lt_options["isRealMobile"] = config.get("isRealMobile", True)
    lt_options["w3c"] = config.get("w3c", True)
    lt_options["plugin"] = config.get("plugin", "python-python")
    lt_options["app"] = config.get("app", "lt://APP10160501071730831350474374")
    # lt_options["appProfiling"] = config.get("appProfiling", True)

    # LambdaTest credentials
    username = os.environ.get("LT_USERNAME", config.get("lambdatest_username", "username"))
    accesskey = os.environ.get("LT_ACCESS_KEY", config.get("lambdatest_access_key", "accesskey"))

    # Set options based on the platform
    if platform == "android":
        options = UiAutomator2Options()
        lt_options["app"] = "lt://APP10160351951731330513576557"
        lt_options["name"] = "Android Test"
        lt_options["customFlutterLaunch"] = True
        lt_options["automationName"] = "Flutter"
        lt_options["appiumVersion"] = "2.4.1"

    elif platform == "ios":
        options = XCUITestOptions()
        lt_options["app"] = "lt://APP10160501071730831350474374"
        lt_options["name"] = "iOS Test"
        lt_options["customFlutterLaunch"] = True
        lt_options["appiumVersion"] = "2.4.1"
        lt_options["automationName"] = "Flutter"
        lt_options["platformVersion"] = "16"
    else:
        raise ValueError(f"Invalid platform: {platform}")

    # Set LT:Options capabilities
    options.set_capability("LT:Options", lt_options)

    # Initialize the remote driver with LambdaTest Hub URL
    lt_url = f"https://{username}:{accesskey}@mobile-hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(command_executor=lt_url, options=options)
    
    return driver