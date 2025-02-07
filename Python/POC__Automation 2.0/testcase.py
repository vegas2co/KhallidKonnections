'''
Webpage Object Modal Automation
By: Khallid Williams
Testing Google, Facebook, Youtube, Yahoo Mail.

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
        bing_page = actions.FreeStylePage(self.driver)
        assert_page = assertions.MainPage(self.driver)

        self.assertTrue(assert_page.is_title_matches('Search - Microsoft Bing'), "bing.com title doesn't match.")
        bing_page.navigateToBing()
        bing_page.openNewTab()
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
        travel_page = actions.GoogleTravelBot(self.driver)
        assert_travel_page = assertions.GoogleTravelBot(self.driver)
        assert_main = assertions.MainPage(self.driver)
    
        assert_main.is_title_matches('Google Flights - Find Cheap Flight Options & Track Prices'), "google.com title doesn't match."
        travel_page.navigateToGoogleTravel()
        travel_page.testSearchFlights('New York', '2025-03-05', '2025-03-10')
        assert_travel_page.is_top_departing_flights()
        travel_page.testPurchseFlight()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(YoutubeSearch())
    