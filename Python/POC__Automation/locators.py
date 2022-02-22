from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    GO_BUTTON = (By.ID, 'submit')
    SEARCH_BOX = (By.ID, 'id-search-field')
    GOOGLE_SEARCH_BOX = (By.NAME, 'btnK')
    KhallidKonnectionsLink = (By.CSS_SELECTOR, '#rso > div:nth-child(1) > div > div:nth-child(1) > div > div > div.NJo7tc.Z26q7c.jGGQ5e > div > a > h3')
    YouTube_Search_Button = (By.ID, 'search-icon-legacy')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    pass