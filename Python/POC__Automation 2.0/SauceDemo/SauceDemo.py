import unittest
from selenium import webdriver
import assertions
import actions
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

class SauceDemoTest(unittest.TestCase):
    def setUp(self):
        self.PATH = Service('/Users/khallidwilliams/Desktop/Khallid Konnections/geckodriver')
        self.driver = webdriver.Firefox(service=self.PATH)
        self.driver.get("https://www.saucedemo.com")

    def test(self):
        self.driver.maximize_window()
        base = actions.BasePage(self.driver)
        action = actions.SauceDemo(self.driver)
        asserts = assertions.SauceDemo(self.driver)

        action.login("standard_user", "secret_sauce")
        action.clickLogin()
        asserts.is_title_matches("Swag Labs")
        action.clickSauceLabsBackPack()
        asserts.is_item_title_matches("Sauce Labs Backpack")
        action.clickAddToCart()
        action.clickBackToProducts()
        action.add_tshirt_to_cart()
        action.add_fleece_jacket_to_cart()
        action.click_cart()
        base.scroll(200)
        sleep(2)
        action.click_checkout()
        action.fill_out_form("Quality", "Assurance", "89106")
        action.continueButton()
        base.scroll(320)
        base.takeScreenShot("SauceDemo")
        action.finishButton()
        asserts.is_purchase_success("Thank you for your order!")
        sleep(2)
        action.backHomeButton()
        asserts.is_title_matches("Swag Labs")
        action.logout()

    def tearDown(self):
        return super().tearDown()
    
if __name__ == "__main__":
    unittest.main()