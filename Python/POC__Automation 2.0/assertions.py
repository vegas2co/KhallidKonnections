from elements import BasePageElement
from locators import MainPageLocators
from selenium.webdriver.common.keys import Keys
from time import sleep

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'q'

class SearchTextElementYT(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'search_query'


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def is_title_matches(self, website):
        """Verifies that the hardcoded text "Python" appears in page title"""

        return website in self.driver.title
        
class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
    
class YahooLogin(BasePage):
    """Search results page action methods come here"""

    def is_confirm_login(self):
        try:
            self.driver.find_element(*MainPageLocators.Yahoo_Confirm_Signin).click()
        except:
            print('Already signed in')

    def is_inbox_loaded(self):
        return "Inbox" in self.driver.page_source
    
class QADemo(BasePage):
    """Search results page action methods come here"""

class FreeStylePage(BasePage):
    """Search results page action methods come here"""

class GoogleTravelBot(BasePage):

    def is_top_departing_flights(self):
        self.driver.find_element(*MainPageLocators.TopFlightsText)