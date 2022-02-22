from Actions.Automation1_Actions import *
from Elements.Automation1_Elements import *

#Test Case 1 - Navigate to Google and Search Khallid Konnections
EXPAND_WINDOW
#select_gmail


#Yahoo Login
navigate_to_webpage("https://yahoo.com")
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

