'''
Webpage Object Modal Automation
By: Khallid Williams
Testing Google, Facebook, Youtube, Yahoo Mail, QaDemo, Google Flights, Nike.

Notes:
YOUTUBE does not like Keys.ENTER
'''

import unittest
from selenium import webdriver
import assertions
import actions
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

G_KK = 'Khallid Konnections' + Keys.RETURN

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.PATH = Service('/Users/khallidwilliams/Desktop/Khallid Konnections/geckodriver')
        self.driver = webdriver.Firefox(service=self.PATH)
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""

        #Load the main page. In this case the home page of Python.org.
        action = actions.MainPage(self.driver)
        assertion = assertions.MainPage(self.driver)

        #Checks if the word "Python" is in title
        self.assertTrue(assertion.is_title_matches('Python'), "python.org title doesn't match.")
        #Sets the text of search textbox to "pycon"
        action.search_text_element = "pycon"
        action.click_go_button()
        search_results_page = actions.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        self.assertTrue(search_results_page.is_results_found(), "No results found.")

    def tearDown(self):
        self.driver.close()

class GoogleSearch(unittest.TestCase):
    """A sample test class to navigate to google and type in Khallid Konnections"""

    def setUp(self):
        self.PATH = Service('/Users/khallidwilliams/Desktop/Khallid Konnections/geckodriver')
        self.driver = webdriver.Firefox(service=self.PATH)
        self.driver.get("https://www.google.com")

    def test_search_in_google(self):
        self.driver.maximize_window()
        action = actions.MainPage(self.driver)
        assertion = assertions.MainPage(self.driver)

        self.assertTrue(assertion.is_title_matches('Google'), "google.com title doesn't match.")
        action.search_text_element = G_KK
        sleep(3)

        action.click_khallid_konnections_link()
        sleep(3)
        search_results_page = assertion.SearchResultsPage(self.driver)

        #Scroll down
        scrolldownLength = [500,700,900,1100]
        for i in scrolldownLength:
            action.scroll(i)
        sleep(4)
        self.assertTrue(search_results_page.is_results_found(), "No results found.")

    def tearDown(self):
        self.driver.close()

class YoutubeSearch(unittest.TestCase):
    """A sample test class to play a video and make it full screen"""

    def setUp(self):
        self.PATH = Service('/Users/khallidwilliams/Desktop/Khallid Konnections/geckodriver')
        self.driver = webdriver.Firefox(service=self.PATH)
        self.driver.get("http://www.youtube.com")

    def test_search_in_youtube(self):
        self.driver.maximize_window()
        action = actions.MainPage(self.driver)
        assertion = assertions.MainPage(self.driver)
        assertionSearch = assertions.SearchResultsPage(self.driver)

        self.assertTrue(assertion.is_title_matches('YouTube'), "youtube.com title doesn't match.")
        action.search_text_element_YT = 'Khallid Konnect'
        sleep(1)
        action.click_youtube_search_button()
        #Verifies that the results page is not empty
        self.assertTrue(assertionSearch.is_results_found(), "No results found.")
        sleep(3)
        action.click_khallid_konnections_page()
        sleep(2)
        action.click_khallid_konnections_page()
        sleep(13)

    def tearDown(self):
        self.driver.close()

class YahooMail(unittest.TestCase):
    """A sample test class to login to Yahoo Mail and search for Khallid Konnections"""

    def setUp(self):
        self.PATH = Service('/Users/khallidwilliams/Desktop/Khallid Konnections/geckodriver')
        self.driver = webdriver.Firefox(service=self.PATH)
        self.driver.get("https://mail.yahoo.com")

    def test_login_yahoo_mail(self):
        self.driver.maximize_window()
        action = actions.YahooLogin(self.driver)
        assertionMain = assertions.MainPage(self.driver)
        assertionYahoo = assertions.YahooLogin(self.driver)

        self.assertTrue(assertionMain.is_title_matches('Yahoo Mail'), "Yahoo Mail title doesn't match.")
        action.login_to_yahoo_mail('williams_khallid@yahoo.com', 'Valerie72')
        assertionYahoo.is_confirm_login()
        action.search_yahoo_mail("khallid konnections")
        sleep(7)
        assertionYahoo.is_inbox_loaded(), "Inbox not loaded."

    def tearDown(self):
        self.driver.close()

class DemoQA(unittest.TestCase):
    """A sample test class to navigate to demoqa and fill out a form"""

    def setUp(self):
        self.PATH = Service('/Users/khallidwilliams/Desktop/Khallid Konnections/geckodriver')
        self.driver = webdriver.Firefox(service=self.PATH)
        self.driver.get("https://demoqa.com/automation-practice-form")

    def test_demoqa(self):
        self.driver.maximize_window()
        qa_page = actions.QADemo(self.driver)
        assertion = assertions.MainPage(self.driver)

        self.assertTrue(assertion.is_title_matches('DEMOQA'), "demoqa.com title doesn't match.")
        qa_page.fill_out_form('Khallid', 'Williams', 'qadummy@test.com', '1234567890', '1234 Test St', 'Math')

    def tearDown(self):
        self.driver.close()

class BingSearch(unittest.TestCase):
    """A sample test class to navigate to bing and search for Khallid Konnections"""

    def setUp(self):
        self.PATH = Service('/Users/khallidwilliams/Desktop/Khallid Konnections/geckodriver')
        self.driver = webdriver.Firefox(service=self.PATH)
        self.driver.get("https://www.bing.com")

    def test_search_in_bing(self):
        self.driver.maximize_window()
        base_page = actions.BasePage(self.driver)
        bing_page = actions.FreeStylePage(self.driver)
        assert_page = assertions.MainPage(self.driver)

        self.assertTrue(assert_page.is_title_matches('Search - Microsoft Bing'), "bing.com title doesn't match.")
        base_page.navigateTo('http://bing.com/')
        bing_page.openNewTab(1)
        base_page.navigateTo('http://stackoverflow.com/')
        bing_page.closeTab()
        bing_page.searchSuperBowls('Super Bowls')
        bing_page.takeScreenShot()

    def tearDown(self):
        self.driver.close()

class GoogleTravelBot(unittest.TestCase):
    """A sample test class to navigate to google travel and search for a flight"""

    def setUp(self):
        self.PATH = Service('/Users/khallidwilliams/Desktop/Khallid Konnections/geckodriver')
        self.driver = webdriver.Firefox(service=self.PATH)

    def testSearchFlights(self):
        self.driver.maximize_window()
        base_page = actions.BasePage(self.driver)
        travel_page = actions.GoogleTravelBot(self.driver)
        assert_travel_page = assertions.GoogleTravelBot(self.driver)
        assert_main = assertions.MainPage(self.driver)
    
        assert_main.is_title_matches('Google Flights - Find Cheap Flight Options & Track Prices'), "google.com title doesn't match."
        base_page.navigateTo('https://www.google.com/travel/flights?gl=US&hl=en-US')
        travel_page.testSearchFlights('New York', '2025-03-05', '2025-03-10')
        assert_travel_page.is_departing_flights_list()
        travel_page.testDepartFlight()
        assert_travel_page.is_returning_flights_list()
        travel_page.testReturnFlight()
        travel_page.clickContinueButton()

    def tearDown(self):
        self.driver.close()

class NikeSearch(unittest.TestCase):
    """A sample test class to navigate to nike and search for a shoe"""

    def setUp(self):
        self.PATH = Service('/Users/khallidwilliams/Desktop/Khallid Konnections/geckodriver')
        self.driver = webdriver.Firefox(service=self.PATH)
        self.driver.get("https://www.nike.com")

    def test_search_in_nike(self):
        base_page = actions.BasePage(self.driver)
        nike_page = actions.NikeBot(self.driver)
        assert_page = assertions.MainPage(self.driver)
        assert_page_nike = assertions.NikeBot(self.driver)

        #Search first shoe Airmax Plus
        self.driver.maximize_window()
        assert_page.is_title_matches('Nike')
        nike_page.searchNike('Airmax')
        assert_page_nike.is_nike_search_results_displayed()
        nike_page.clickAirMaxButton()
        assert_page_nike.is_nike_search_results_displayed()
        nike_page.selectNikeShoe()
        assert_page_nike.is_nike_shoe_name_displayed("Nike Air Max Plus OG")
        base_page.scroll(200)
        nike_page.selectNikeSize()
        base_page.scroll(500)
        nike_page.addToCart()
        assert_page_nike.is_bot_modal_present()
        nike_page.exit_modal()
        base_page.takeScreenShot("AirMaxPlus")

        #Search first shoe Jordan 1
        base_page.scroll(-500)
        nike_page.searchNike('Jordan 1')
        assert_page_nike.is_nike_search_results_displayed()
        nike_page.selectNikeShoe()
        assert_page_nike.is_nike_shoe_name_displayed("Air Jordan 1 Retro High OG \"Black Toe\"")
        base_page.scroll(200)
        base_page.takeScreenShot("Jordan1")

    def tearDown(self):
        self.driver.close()

class Airlines(unittest.TestCase):
    """A sample test class to navigate to airlines and search for a flight""" 
    
    def setUp(self):
        self.PATH = Service('/Users/khallidwilliams/Desktop/Khallid Konnections/geckodriver')
        self.driver = webdriver.Firefox(service=self.PATH)
        
    def test_search_in_airlines(self):
        self.driver.maximize_window()
        base_page = actions.BasePage(self.driver)
        action_aa = actions.AmericanAirlinesBot(self.driver)
        assert_aa = assertions.AmericanAirlinesBot(self.driver)

        base_page.navigateTo('https://www.aa.com/homePage.do')
        base_page.scroll(300)      
        assert_aa.is_book_trip_present()
        action_aa.enter_flight_info('NYC', 'LAX', '03/12/2025', '03/17/2025')
        sleep(5)
        action_aa.submit_flight()

        #depart
        assert_aa.is_flights_header_present()
        assert_aa.is_departing_header_matching("Choose flights")
        action_aa.choose_departing_flight() 
        base_page.scroll(1000)
        action_aa.select_departing_flight()

        #return
        assert_aa.is_returning_header_matching("Choose flights")
        base_page.scroll(600)   
        sleep(10)
        action_aa.choose_returning_flgihts()
        base_page.scroll(1500)
        sleep(2)
        action_aa.select_returning_flight()

        #confimation
        assert_aa.is_upgrade_to_main_plus_modal_present()
        action_aa.click_upgrade_to_main_plus_modal_exit()
        base_page.scroll(2500)
        assert_aa.is_continue_as_guest_button_present()
        action_aa.click_continue_as_guess_button()

        base_page.scroll(500)
        action_aa.enter_first_name("Quality")
        action_aa.enter_last_name("Assurance")
        action_aa.click_month(5)
        action_aa.click_day(13)
        action_aa.click_year(50)
        action_aa.click_gender(1)
        action_aa.click_country(1)
        action_aa.click_state(46)
        action_aa.enter_email('qa@test.com')
        action_aa.enter_confirm_email('qa@test.com')
        action_aa.click_primary_phone_dropdown(0)
        action_aa.enter_primary_phone('2145559865')
        base_page.scroll(2500)
        action_aa.click_continue_button()
        sleep(20)

        #Seats
        base_page.scroll(200)
        sleep(2)
        action_aa.click_skip_seats_button()

        #PayNow
        action_aa.click_credit_debit_card_radio_button()
        action_aa.fill_out_credit_card_info('Quality','Assurance','4111111111111111','0129','123 Main St','Dallas','Texas',9,'75002')
        assert_aa.is_terms_and_conditions_present()
        action_aa.click_terms_and_conditons()
        assert_aa.is_pay_now_button_present()
        #action_aa.click_pay_now_button()


class TestClass(unittest.TestCase):
    def setUp(self):
        self.PATH = Service('/Users/khallidwilliams/Desktop/Khallid Konnections/geckodriver')
        self.driver = webdriver.Firefox(service=self.PATH)

    def test_aa(self):
        test_american_airlines = Airlines()
        test_american_airlines.setUp()
        test_american_airlines.test_search_in_airlines()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(TestClass())