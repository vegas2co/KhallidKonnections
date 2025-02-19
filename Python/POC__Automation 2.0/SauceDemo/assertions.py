from locators import SauceDemoLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import actions

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

class SauceDemo(BasePage):
    """Home page action methods come here SauceDemo"""

    def is_title_matches(self, header_text):
        header = self.driver.find_element(*SauceDemoLocators.header).text
        assert header == header_text, f"Expected header to be '{header_text}', but got '{header}'"

    def is_item_title_matches(self, item_text):
        header = self.driver.find_element(*SauceDemoLocators.item_title).text
        assert header == item_text, f"Expected header to be '{item_text}', but got '{header}'"

    def is_purchase_success(self, success_message):
        header = self.driver.find_element(*SauceDemoLocators.success).text
        assert header == success_message, f"Expected header to be '{success_message}', but got '{header}'"