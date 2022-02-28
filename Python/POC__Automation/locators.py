from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    #PYTHON
    GO_BUTTON = (By.ID, 'submit')
    SEARCH_BOX = (By.ID, 'id-search-field')

    #GOOGLE
    KhallidKonnectionsLink = (By.CSS_SELECTOR, '#rso > div:nth-child(2) > div > div:nth-child(1) > div > div > div.NJo7tc.Z26q7c.jGGQ5e > div > a > h3')
    
    #YOUTUBE
    YouTube_Search_Button = (By.ID, 'search-icon-legacy')
    Click_KK_Video = (By.LINK_TEXT, 'Khallid Konnect')
    Full_Screen_Video = (By.CSS_SELECTOR, '#c4-player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button.ytp-fullscreen-button.ytp-button')
