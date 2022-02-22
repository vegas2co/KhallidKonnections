from elements import BasePageElement
from locators import MainPageLocators
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

    def scroll(self, Y):
        self.driver.execute_script("window.scrollTo(0, "+str(Y)+")")
        sleep(2)


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()
    search_text_element_YT = SearchTextElementYT()

    def is_title_matches(self, website):
        """Verifies that the hardcoded text "Python" appears in page title"""

        return website in self.driver.title

    def click_go_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    def click_search_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.GOOGLE_SEARCH_BOX)
        element.click()

    def click_khallid_konnections_link(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.KhallidKonnectionsLink)
        element.click()

    def click_youtube_search_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.YouTube_Search_Button)
        element.click()
        
class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source

    def is_google_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source