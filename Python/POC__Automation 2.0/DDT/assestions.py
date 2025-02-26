from locators import SauceDemoLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

class SauceDemo(BasePage):
    """Home page action methods come here SauceDemo"""

    def is_login_title_present(self):        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.driver.find_element(*SauceDemoLocators.login_title))
            )
            print("Swag Labs is present")
        except:
            print("Element is not present")

    def is_title_matches(self, header_text):
        header = self.driver.find_element(*SauceDemoLocators.header).text
        assert header == header_text, f"Expected header to be '{header_text}', but got '{header}'"

    def is_item_title_matches(self, item_text):
        header = self.driver.find_element(*SauceDemoLocators.item_title).text
        assert header == item_text, f"Expected header to be '{item_text}', but got '{header}'"

    def is_purchase_success(self, success_message):
        header = self.driver.find_element(*SauceDemoLocators.success).text
        assert header == success_message, f"Expected header to be '{success_message}', but got '{header}'"

    def is_logged_in(self):
        assert "inventory.html" in self.driver.current_url, "Login failed!"
        print('Logged in  to',self.driver.current_url)
    
    def is_form_present(self):
        fname = self.driver.find_element(*SauceDemoLocators.first_name)
        lname = self.driver.find_element(*SauceDemoLocators.last_name)
        zip_ = self.driver.find_element(*SauceDemoLocators.zip)
        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located([fname,lname,zip_])
            )
            print("Elements are present")
        except:
            print("Elements are not present")

    def is_continueButton_present(self):
        button = self.driver.find_element(*SauceDemoLocators.continue_button)
        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(button)
            )
            print("Element is present")
        except:
            print("Element is not present")

    def is_finishButton_present(self):
        button = self.driver.find_element(*SauceDemoLocators.finish_button)
        
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(button)
            )
            print("Element is present")
        except:
            print("Element is not present")