from locators import SauceDemoLocators
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

    def scroll(self, Y):
        self.driver.execute_script("window.scrollTo(0, "+str(Y)+")")
        sleep(2)

    def takeScreenShot(self, name):
        self.driver.save_screenshot('/Users/khallidwilliams/Desktop/Khallid Konnections/Python/POC__Automation 2.0/SauceDemo/'+ name +'.png')
        sleep(2)
        print("Screenshot taken")

class SauceDemo(BasePage):
    def login(self, username, password):
        self.driver.find_element(*SauceDemoLocators.username).click()
        self.driver.find_element(*SauceDemoLocators.username).send_keys(username)
    
        self.driver.find_element(*SauceDemoLocators.password).click()
        self.driver.find_element(*SauceDemoLocators.password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*SauceDemoLocators.loginButton).click()

    def clickSauceLabsBackPack(self):
        self.driver.find_element(*SauceDemoLocators.sauce_labs_backpack).click()

    def clickAddToCart(self):
        self.driver.find_element(*SauceDemoLocators.add_to_card).click()

    def clickBackToProducts(self):
        self.driver.find_element(*SauceDemoLocators.back_to_products).click()

    def add_tshirt_to_cart(self):
        self.driver.find_element(*SauceDemoLocators.tshirt_add_to_card).click()

    def add_fleece_jacket_to_cart(self):
        self.driver.find_element(*SauceDemoLocators.fleece_jacket_add_to_card).click()

    def click_cart(self):
        self.driver.find_element(*SauceDemoLocators.cart).click()

    def click_checkout(self):
        self.driver.find_element(*SauceDemoLocators.checkout_button).click()

    def fill_out_form(self,firstname, lastname, zipcode):
        self.driver.find_element(*SauceDemoLocators.first_name).click()
        self.driver.find_element(*SauceDemoLocators.first_name).send_keys(firstname)

        self.driver.find_element(*SauceDemoLocators.last_name).click()
        self.driver.find_element(*SauceDemoLocators.last_name).send_keys(lastname)

        self.driver.find_element(*SauceDemoLocators.zip).click()
        self.driver.find_element(*SauceDemoLocators.zip).send_keys(zipcode)

    def continueButton(self):
        self.driver.find_element(*SauceDemoLocators.continue_button).click()

    def finishButton(self):
        self.driver.find_element(*SauceDemoLocators.finish_button).click()

    def backHomeButton(self):
        self.driver.find_element(*SauceDemoLocators.back_home).click()

    def logout(self):
        self.driver.find_element(*SauceDemoLocators.menu).click()