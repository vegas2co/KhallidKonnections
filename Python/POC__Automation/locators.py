from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    #PYTHON
    GO_BUTTON = (By.ID, 'submit')
    SEARCH_BOX = (By.ID, 'id-search-field')

    #GOOGLE
    KhallidKonnectionsLink = (By.CSS_SELECTOR, '#rso > div:nth-child(2) > div > div:nth-child(1) > div > div > div.NJo7tc.Z26q7c.jGGQ5e > div > a > h3')
    
    #YOUTUBE
    YouTube_Search_Button = (By.XPATH, '/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[2]/yt-searchbox/button')
    Click_KK_Video = (By.LINK_TEXT, 'Khallid Konnect')
    Full_Screen_Video = (By.CSS_SELECTOR, '#c4-player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button.ytp-fullscreen-button.ytp-button')

    #YAHOO
    Yahoo_Signin = (By.XPATH, '/html/body/div[1]/a')
    Yahoo_Username = (By.XPATH, '//*[@id="login-username"]')
    Yahoo_Next_Button = (By.XPATH, '//*[@id="login-signin"]')
    Yahoo_Password = (By.XPATH, '//*[@id="login-passwd"]')
    Yahoo_Confirm_Signin = (By.XPATH, '//*[@id="login-signin"]')
    Yahoo_SearchBox = (By.XPATH, '/html/body/header/div/div/div[3]/div/div[2]/div/div/div/div[1]/ul/li/div/div/input[1]')

    #QADEMO
    QADemo_FirstName = (By.XPATH, '//*[@id="firstName"]')
    QADemo_LastName = (By.XPATH, '//*[@id="lastName"]')
    QADemo_Email = (By.XPATH, '//*[@id="userEmail"]')
    QADemo_Phone = (By.XPATH, '//*[@id="userNumber"]')
    QADemo_Subject = (By.XPATH, '//*[@id="subjectsInput"]')
    QADemo_Address = (By.XPATH, '//*[@id="currentAddress"]')
    QADemo_submitButton = (By.XPATH, '//*[@id="submit"]')

    

