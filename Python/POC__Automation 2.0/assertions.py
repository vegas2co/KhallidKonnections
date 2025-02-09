from elements import BasePageElement
from locators import MainPageLocators
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    def is_departing_flights_list(self):
        #This captures the flight information
        flights = self.driver.find_elements(*MainPageLocators.DepartFlightList)
        flight_data = []
        for flight in flights:
            try:
                flight_time = flight.find_element(*MainPageLocators.DepartFlightTime).text
                flight_length = flight.find_element(*MainPageLocators.DepartFlightLength).text
                non_stops = flight.find_element(*MainPageLocators.DepartNonStops).text
                price = flight.find_element(*MainPageLocators.DepartFlightPrice).text
                flight_data.append({
                    'flight_time': flight_time,
                    'flight_length': flight_length,
                    'non_stops': non_stops,
                    'price': price
            })
            except NoSuchElementException:
                continue
            print(flight_data)
            print('done with arriving flight info')
        return flight_data

    def is_returning_flights_list(self):
        #This captures the flight information
        flights = self.driver.find_elements(*MainPageLocators.ReturnFlightList)
        flight_data = []
        for flight in flights:
            try:
                flight_time = flight.find_element(*MainPageLocators.ReturnFlightTime).text
                flight_length = flight.find_element(*MainPageLocators.ReturnFlightLength).text
                non_stops = flight.find_element(*MainPageLocators.ReturnNonStops).text
                price = flight.find_element(*MainPageLocators.ReturnFlightPrice).text
                flight_data.append({
                    'flight_time': flight_time,
                    'flight_length': flight_length,
                    'non_stops': non_stops,
                    'price': price
            })
            except NoSuchElementException:
                continue
            print(flight_data)
            print('done with flight departing info')
        return flight_data

class NikeBot(BasePage):

    def is_nike_search_results(self):
        return "Nike" in self.driver.page_source
    
    def is_bot_modal_present(self):
        try:
            modal = self.driver.find_element(*MainPageLocators.Nike_Error_Message_Modal)
            modal_title = self.driver.find_element(*MainPageLocators.Nike_Error_Message_Modal_Title)
            modal_text = self.driver.find_element(*MainPageLocators.Nike_Error_Message_Modal_Text)
            assert modal.is_displayed(), "Modal is present but not displayed"
            assert modal_title.is_displayed(), "Modal Title is present but not displayed"
            assert modal_text.is_displayed(), "Modal Text is present but not displayed"
        except NoSuchElementException:
            self.fail("Modal is not present")

    def is_nike_search_results_displayed(self):
        try:
            search_results = self.driver.find_element(*MainPageLocators.Nike_Search_Results)
            search_name = self.driver.find_element(*MainPageLocators.Nike_Search_Name)
            assert search_results.is_displayed(), "Search Results are present but not displayed"
            assert search_name.is_displayed(), "Search Name is present but not displayed"
        except NoSuchElementException:
            self.fail("Search Results are not present")

    def is_nike_shoe_name_displayed(self, shoe_text):
        try:
            shoe_name = self.driver.find_element(*MainPageLocators.Nike_Shoe_Name)
            shoe_name_title = self.driver.find_element(*MainPageLocators.Nike_Shoe_Name).text
            assert shoe_name.is_displayed(), "Shoe Name is present but not displayed"
            assert shoe_name_title == shoe_text, f"Expected shoe name to be '{shoe_text}', but got '{shoe_name_title}'"
        except NoSuchElementException:
            self.fail("Shoe Name is not present")