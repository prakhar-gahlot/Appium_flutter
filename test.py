import unittest
from driver_factory import get_driver
from appium.webdriver.common import appiumby
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locatorSupply import LocatorHelper
from appium_flutter_finder import FlutterElement
from appium_flutter_finder.flutter_finder import FlutterFinder

import time
class AppiumTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()
        platform = cls.driver.capabilities['platformName']
        cls.locator_helper = LocatorHelper(platform)

    def test_sample(self):
        # Sample test logic using the driver
        print("Running test on", self.driver.capabilities['platformName'])

        finder = FlutterFinder()
        time.sleep(30)
        # render_tree = self.driver.execute_script("flutter: getRenderTree")
        # print(render_tree)
        # text_finder = finder.by_value_key("username")
        # text_element = FlutterElement(self.driver, text_finder)
        
        # text_element.click()
        
        usernameL = self.locator_helper.get_username_element_locator()
        username = FlutterElement(self.driver,usernameL)
        username.click()
        username.send_keys("Prakhar")

        passwordFieldlocator = self.locator_helper.get_password_element_locator()
        passwordField = FlutterElement(self.driver,passwordFieldlocator)
        passwordField.click()
        passwordField.send_keys("Mypassword")

        time.sleep(5)

        loginLocator = self.locator_helper.get_login_locator()
        login = FlutterElement(self.driver,loginLocator)
        login.click()
        time.sleep(10)


    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
