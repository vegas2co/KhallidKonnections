import unittest
from selenium import webdriver
from import assertions
import actions
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

class OrangeHRM(unittest.TestCase):
    def setUp(self):
        self.PATH = Service('/Users/khallidwilliams/Desktop/Khallid Konnections/geckodriver')
        self.driver = webdriver.Firefox(service=self.PATH)
        self.driver.get("https://www.orangehrm.com")

    def test_search_in_google(self):
        self.driver.maximize_window()
        action = actions.MainPage(self.driver)
        assertion = assertions.MainPage(self.driver)

    def tearDown(self):
        return super().tearDown()
    
if __name__ == "__main__":
    unittest.main()