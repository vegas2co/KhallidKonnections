import unittest
import openpyxl
import assestions
import actions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

# Read data from Excel
class SauceDemoTest(unittest.TestCase):
    def get_test_data(file_path, sheet_name):
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name]
        data = []

        for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip header
            data.append(row)

        workbook.close()
        return data
    
    # Data Provider - Fetch test data from Excel
    test_data = get_test_data("/Users/khallidwilliams/Desktop/Khallid Konnections/Python/POC__Automation 2.0/DDT/testdata.xlsx", "Sheet1")
    print("Loaded test data:", test_data) 

    def loop_thru_list(self):    
        for username, password, title, item_num1, form_fname, form_lname, form_zip, ssName, success_memo in self.test_data:
            with self.subTest(username=username, password=password, title=title, item_num1=item_num1,
                                form_fname=form_fname, form_lname=form_lname, form_zip=form_zip,
                                ssName=ssName, success_memo=success_memo):
                pass

    def setUp(self):
        self.PATH = Service('/Users/khallidwilliams/Desktop/Khallid Konnections/geckodriver')
        self.driver = webdriver.Firefox(service=self.PATH)
        self.driver.get("https://www.saucedemo.com/")
    
    def test_login(self):
        self.driver.maximize_window()
        base = actions.BasePage(self.driver)
        action = actions.SauceDemo(self.driver)
        asserts = assestions.SauceDemo(self.driver)

        row1 = self.test_data[0]
        action.login(row1[0],row1[1])
        asserts.is_login_title_present()
        action.clickLogin()
        asserts.is_logged_in()
        asserts.is_title_matches(row1[2])
        action.clickSauceLabsBackPack()
        asserts.is_item_title_matches(row1[3])
        action.clickAddToCart()
        action.clickBackToProducts()
        action.add_tshirt_to_cart()
        action.add_fleece_jacket_to_cart()
        action.click_cart()
        base.scroll(200)
        sleep(1)
        action.click_checkout()
        asserts.is_form_present()
        action.fill_out_form(row1[4], row1[5], row1[6])
        asserts.is_continueButton_present()
        action.continueButton()
        base.scroll(320)
        base.takeScreenShot(row1[7])
        asserts.is_finishButton_present()
        action.finishButton()
        asserts.is_purchase_success(row1[8])
        sleep(1)
        action.backHomeButton()
        asserts.is_title_matches(row1[2])
        action.logout()

    def test_login_problem_user(self):
        self.driver.maximize_window()
        base = actions.BasePage(self.driver)
        action = actions.SauceDemo(self.driver)
        asserts = assestions.SauceDemo(self.driver)
        row2 = self.test_data[1]
        action.login(row2[0],row2[1])
        action.clickLogin()
        asserts.is_logged_in()

    def test_login_glitch_user(self):
        self.driver.maximize_window()
        base = actions.BasePage(self.driver)
        action = actions.SauceDemo(self.driver)
        asserts = assestions.SauceDemo(self.driver)
        row3 = self.test_data[1]
        action.login(row3[0],row3[1])
        action.clickLogin()
        asserts.is_logged_in()

    def tearDown(self):
        return super().tearDown()
    
if __name__ == "__main__":
    unittest.main()