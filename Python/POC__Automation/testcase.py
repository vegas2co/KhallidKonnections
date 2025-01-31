'''
Webpage Object Modal Automation
By: Khallid Williams
Testing Google, Facebook, Youtube, Yahoo Mail.

Notes:
YOUTUBE does not like Keys.ENTER
'''

import unittest
from selenium import webdriver
import page
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
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        self.assertTrue(main_page.is_title_matches('Python'), "python.org title doesn't match.")
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        self.assertTrue(search_results_page.is_results_found(), "No results found.")

    def tearDown(self):
        self.driver.close()

class GoogleSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.PATH = Service('/Users/khallidwilliams/Desktop/Khallid Konnections/geckodriver')
        self.driver = webdriver.Firefox(service=self.PATH)
        self.driver.get("https://www.google.com")

    def test_search_in_google(self):
        main_page = page.MainPage(self.driver)
        self.assertTrue(main_page.is_title_matches('Google'), "google.com title doesn't match.")
        main_page.search_text_element = G_KK
        sleep(3)
        main_page.click_khallid_konnections_link()
        sleep(3)
        search_results_page = page.SearchResultsPage(self.driver)

        #Scroll down
        scrolldownLength = [500,700,900,1100]
        for i in scrolldownLength:
            main_page.scroll(i)
        sleep(4)
        self.assertTrue(search_results_page.is_results_found(), "No results found.")

    def tearDown(self):
        self.driver.close()

class YoutubeSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.PATH = Service('/Users/khallidwilliams/Desktop/Khallid Konnections/geckodriver')
        self.driver = webdriver.Firefox(service=self.PATH)
        self.driver.get("http://www.youtube.com")

    def test_search_in_youtube(self):
        main_page = page.MainPage(self.driver)
        self.assertTrue(main_page.is_title_matches('YouTube'), "youtube.com title doesn't match.")
        main_page.search_text_element_YT = 'Khallid Konnect'
        sleep(1)
        main_page.click_youtube_search_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        self.assertTrue(search_results_page.is_results_found(), "No results found.")
        sleep(3)
        main_page.click_khallid_konnections_page()
        sleep(2)
        main_page.click_khallid_konnections_page()
        sleep(120)

    def tearDown(self):
        self.driver.close()

class YahooMail(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.PATH = Service('/Users/khallidwilliams/Desktop/Khallid Konnections/geckodriver')
        self.driver = webdriver.Firefox(service=self.PATH)
        self.driver.get("https://mail.yahoo.com")

    def test_login_yahoo_mail(self):
        yahoo_page = page.YahooLogin(self.driver)
        main_page = page.MainPage(self.driver)
        self.assertTrue(main_page.is_title_matches('Yahoo Mail'), "mail.yahoo.com title doesn't match.")
        yahoo_page.login_to_yahoo_mail('williams_khallid@yahoo.com', 'Valerie72')
        yahoo_page.confirm_login()
        yahoo_page.search_yahoo_mail("khallid konnections")
        sleep(7)
        self.assertTrue(yahoo_page.is_inbox_loaded(), "Inbox not loaded.")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(YahooMail()) #Add class to test one by YoutubeSearch
    