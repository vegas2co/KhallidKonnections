from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

PATH = '/Users/khallidwilliams/Desktop/Khallid Konnections/chromedriver'
driver = webdriver.Chrome(PATH)
EXPAND_WINDOW = driver.maximize_window()

#GOOGLE
access_google = driver.get("https://www.google.com")

click_searchbar = driver.find_element_by_class_name("CcAdNb").click()

#no_thanks_button = driver.find_element_by_id("yDmH0d").click()

click_hamburger_menu = driver.find_element_by_class_name("gb_Qc").click()

click_gmail = driver.find_element(By.CSS_SELECTOR,"#gb > div > div:nth-child(1) > div > div:nth-child(1) > a").click()

#YAHOO
#click_mail = driver.find_element(By.CSS_SELECTOR, "#ybarMailLink > span.ybar-icon-sprite._yb_9450p._yb_1x2ss").click()