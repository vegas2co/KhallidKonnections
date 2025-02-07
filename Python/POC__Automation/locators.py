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

    #Bing   
    Bing_Search = (By.XPATH, '//*[@id="sb_form_q"]')

    #Google Travel
    GoogleTravelOrigin = (By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div/input')
    GoogleTravelDestination = (By.CSS_SELECTOR, '#i23 > div.e5F5td.vxNK6d > div > div > div.cQnuXe.k0gFV > div > div > input')
    GoogleTravelDestinationClick = (By.CLASS_NAME, 'CwL3Ec')
    GoogleTravelDeparture = (By.CSS_SELECTOR, 'body > c-wiz.zQTmif.SSPGKf > div > div:nth-child(2) > c-wiz > div.cKvRXe > c-wiz > div.vg4Z0e > div:nth-child(1) > div.SS6Dqf.POQx1c > div.AJxgH > div > div.rIZzse > div.bgJkKe.K0Tsu > div > div > div.cQnuXe.k0gFV > div > div > div:nth-child(1) > div > div.GYgkab.YICvqf.kStSsc.ieVaIb > div > input')
    GoogleTravelReturn = (By.CSS_SELECTOR, 'body > c-wiz.zQTmif.SSPGKf > div > div:nth-child(2) > c-wiz > div.cKvRXe > c-wiz > div.vg4Z0e > div:nth-child(1) > div.SS6Dqf.POQx1c > div.AJxgH > div > div.rIZzse > div.bgJkKe.K0Tsu > div > div > div.cQnuXe.k0gFV > div > div > div:nth-child(1) > div > div.GYgkab.YICvqf.lJODHb.qXDC9e > div > input')
    GoogleTravelDateDoneButton = (By.CSS_SELECTOR, 'button.DuMIQc:nth-child(1) > span:nth-child(4)')
    GoogleTravelSearchButton = (By.CSS_SELECTOR, 'body > c-wiz.zQTmif.SSPGKf > div > div:nth-child(2) > c-wiz > div.cKvRXe > c-wiz > div.vg4Z0e > div:nth-child(1) > div.SS6Dqf.POQx1c > div.MXvFbd > div > button')

    DepartFlight = (By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/div/div[2]/div[1]/ul/li[1]')
    ReturnFlight = (By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]')  
    ContinueButton = (By.CSS_SELECTOR, '.DuMIQc')