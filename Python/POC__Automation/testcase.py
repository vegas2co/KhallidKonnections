import unittest
from selenium import webdriver
import page
from time import sleep

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.PATH = '/Users/khallidwilliams/Desktop/Khallid Konnections/chromedriver'
        self.driver = webdriver.Chrome(self.PATH)
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
        self.PATH = '/Users/khallidwilliams/Desktop/Khallid Konnections/chromedriver'
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get("http://www.google.com")

    def test_search_in_google(self):
        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        self.assertTrue(main_page.is_title_matches('Google'), "google.com title doesn't match.")
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "Khallid Konnections"
        sleep(3)
        main_page.click_search_button()
        main_page.click_khallid_konnections_link()
        sleep(3)
        search_results_page = page.SearchResultsPage(self.driver)
        #Scroll down
        scrolldownLength = [500,700,900,1100]
        for i in scrolldownLength:
            main_page.scroll(i)
        sleep(4)
        #Verifies that the results page is not empty
        self.assertTrue(search_results_page.is_google_results_found(), "No results found.")

    def tearDown(self):
        self.driver.close()

class YoutubeSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.PATH = '/Users/khallidwilliams/Desktop/Khallid Konnections/chromedriver'
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get("http://www.youtube.com")

    def test_search_in_youtube(self):
        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        self.assertTrue(main_page.is_title_matches('YouTube'), "youtube.com title doesn't match.")
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element_YT = "Chris Smoove"
        sleep(1)
        main_page.click_youtube_search_button()
        sleep(10)
        '''
        main_page.click_khallid_konnections_link()
        sleep(3)
        search_results_page = page.SearchResultsPage(self.driver)
        #Scroll down
        scrolldownLength = [500,700,900,1100]
        for i in scrolldownLength:
            main_page.scroll(i)
        sleep(4)
        #Verifies that the results page is not empty
        self.assertTrue(search_results_page.is_google_results_found(), "No results found.")
        '''

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()