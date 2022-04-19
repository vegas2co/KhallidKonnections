from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

PATH = '/Users/khallidwilliams/Desktop/Khallid Konnections/chromedriver'
driver = webdriver.Chrome(PATH)

def google():
    EXPAND_WINDOW = driver.maximize_window()
    driver.get("http://www.youtube.com")

#Google Search Bar
'''
navigate_to_webpage("https://google.com")
search_bar = driver.find_element(By.NAME, 'q')
search_bar.click()
search_bar.send_keys("Khallid Konnetions" + Keys.ENTER)

if __name__ == "__main__":
    unittest.main()

'''



'''
driver.find_element(By.CSS_SELECTOR, "#ybarMailLink > span.ybar-icon-sprite._yb_9450p._yb_1x2ss").click()
signin = driver.find_element(By.CSS_SELECTOR, "#signin-main > div.header.clearfix > a")
signin.click()
sleep(3)

email = driver.find_element(By.CSS_SELECTOR, "#login-username")
email.click()
email.send_keys("williams_khallid@yahoo.com")
email.submit()
sleep(3)

password = driver.find_element(By.CSS_SELECTOR, "#login-passwd")
password.click()
password.send_keys("") #Hide Password
password.submit()
print("Successful")

#remindMeLater = driver.find_element(By.CSS_SELECTOR, "#login-body > div.login-box-container > div.login-box.right > div.generic-page.comm-channel-refresher.v2 > form > div.bottom-cta.bottom-sticky.footer-container > a.txt-align-center.escape-hatch.refresher-submit").click()
#select_yahooMail

'''