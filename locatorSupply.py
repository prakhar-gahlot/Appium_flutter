from appium.webdriver.common.appiumby import AppiumBy
from appium_flutter_finder import FlutterElement
# from appium_flutter_finder import flutter_finder as find
from appium_flutter_finder.flutter_finder import FlutterFinder

class LocatorHelper:
    finder = FlutterFinder()
    def __init__(self, platform):
        self.platform = platform.lower()

        
    def get_username_element_locator(self):
        if self.platform == "android":
            finder = FlutterFinder()
            # return finder.by_value_key("Username")
            return finder.by_value_key("username")
            
        elif self.platform == "ios":
            finder = FlutterFinder()
            
            return finder.by_type("TextField")
        else:
            raise ValueError(f"Unsupported platform: {self.platform}")
    def get_password_element_locator(self):
        if self.platform == 'android':
            finder = FlutterFinder()
            return finder.by_value_key("password")


        elif self.platform == 'ios':
            finder = FlutterFinder()
            return finder.by_value_key("password")
        else:
            raise ValueError(f"Unsupported platform: {self.platform}")
        
    def get_login_locator(self):
        if self.platform == 'android':
            finder = FlutterFinder()

            return finder.by_value_key("enter")
        elif self.platform == 'ios':
            finder = FlutterFinder()
            return finder.by_text("login")
        else:
            raise ValueError(f"Unsupported platform: {self.platform}")
