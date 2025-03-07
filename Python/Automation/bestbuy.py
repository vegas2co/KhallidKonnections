# Generated by Selenium IDE
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

class TestSearch55LGTV(unittest.TestCase):
  def setUp(self):
    self.PATH = Service('/Users/khallidwilliams/Desktop/Khallid Konnections/geckodriver')
    self.driver = webdriver.Firefox(service=self.PATH)
    self.driver.get("https://www.bestbuy.com/")
  
  def test_search55LGTV(self):
    # Test name: Search 55' LG TV
    # Step # | name | target | value
    # 2 | click | id=gh-search-input | 
    self.driver.find_element(By.ID, "gh-search-input").click()
    # 3 | type | id=gh-search-input | lg smart tv
    self.driver.find_element(By.ID, "gh-search-input").send_keys("lg smart tv")
    # 4 | click | css=.header-search-icon > .w-300 | 
    self.driver.find_element(By.CSS_SELECTOR, ".header-search-icon > .w-300").click()
    # 6 | click | xpath=//img[@alt='LG - 65” Class UT70 Series LED 4K UHD Smart webOS TV (2024) - Front_Zoom'] | 
    self.driver.find_element(By.XPATH, "//img[@alt=\'LG - 65” Class UT70 Series LED 4K UHD Smart webOS TV (2024) - Front_Zoom\']").click()
    # 7 | runScript | window.scrollTo(0,13) | 
    self.driver.execute_script("window.scrollTo(0,13)")
    # 8 | mouseOver | css=.heading-4 | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".heading-4")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 9 | mouseOver | css=.shadow-none > .m-none | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".shadow-none > .m-none")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 10 | mouseOut | css=.shadow-none > .m-none | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 11 | assertElementPresent | css=.priceView-hero-price > span:nth-child(1) | 
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".priceView-hero-price > span:nth-child(1)")
    assert len(elements) > 0

  def tearDown(self):
    return super().tearDown()

if __name__ == "__main__":
    unittest.main()