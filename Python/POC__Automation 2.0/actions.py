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

    def scroll(self, Y):
        self.driver.execute_script("window.scrollTo(0, "+str(Y)+")")
        sleep(2)

    def takeScreenShot(self, name):
        self.driver.save_screenshot('/Users/khallidwilliams/Downloads/'+ name +'.png')
        sleep(2)
        print("Screenshot taken")

class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()
    search_text_element_YT = SearchTextElementYT()

    def click_go_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    def click_khallid_konnections_link(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.KhallidKonnectionsLink)
        element.click()

    def click_youtube_search_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.YouTube_Search_Button)
        element.click()

    def click_khallid_konnections_page(self):
        """Triggers the search"""

        try:
            element = self.driver.find_element(*MainPageLocators.Click_KK_Video)
            element.click()
        except:
            element = self.driver.find_element(*MainPageLocators.Full_Screen_Video)
            element.click()
        
class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    
class YahooLogin(BasePage):
    """Search results page action methods come here"""

    def login_to_yahoo_mail(self, username, password):
        self.driver.find_element(*MainPageLocators.Yahoo_Signin).click()
        self.driver.find_element(*MainPageLocators.Yahoo_Username).send_keys(username)
        self.driver.find_element(*MainPageLocators.Yahoo_Next_Button).click()
        sleep(2)
        self.driver.find_element(*MainPageLocators.Yahoo_Password).send_keys(password)
        self.driver.find_element(*MainPageLocators.Yahoo_Next_Button).click()
    
    def search_yahoo_mail(self, search):
        self.driver.find_element(*MainPageLocators.Yahoo_SearchBox).send_keys(search)
        self.driver.find_element(*MainPageLocators.Yahoo_SearchBox).send_keys(Keys.RETURN)
    
class QADemo(BasePage):
    """Search results page action methods come here"""

    def fill_out_form(self, firstname, lastname, email, phone, address, subject):
        self.driver.find_element(*MainPageLocators.QADemo_FirstName).send_keys(firstname)
        self.driver.find_element(*MainPageLocators.QADemo_LastName).send_keys(lastname)
        self.driver.find_element(*MainPageLocators.QADemo_Email).send_keys(email)
        self.driver.find_element(*MainPageLocators.QADemo_Phone).send_keys(phone)
        sleep(3)
        self.driver.find_element(*MainPageLocators.QADemo_Subject).send_keys(subject)
        self.driver.find_element(*MainPageLocators.QADemo_Address).send_keys(address)
        #self.driver.find_element(*MainPageLocators.QADemo_submitButton).click()

class FreeStylePage(BasePage):

    def navigateToBing(self):
        self.driver.get("http://www.bing.com")
        sleep(2)
    
    def openNewTab(self):
        self.driver.execute_script("window.open('');") #open tab
        self.driver.switch_to.window(self.driver.window_handles[1]) #switch to tab
        self.driver.get('http://stackoverflow.com/')
        sleep(2)
    
    def closeTab(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0]) #switch back to original tab

    def searchSuperBowls(self, search):
        self.driver.find_element(*MainPageLocators.Bing_Search).send_keys(search)
        self.driver.find_element(*MainPageLocators.Bing_Search).send_keys(Keys.RETURN)
        sleep(4)

    def takeScreenShot(self):
        self.driver.save_screenshot('/Users/khallidwilliams/Downloads/SuperBowlScreenShot.png')
        sleep(2)
        print("Screenshot taken")

class GoogleTravelBot(BasePage):

    def navigateToGoogleTravel(self):
        self.driver.get("https://www.google.com/travel/flights?gl=US&hl=en-US")
        sleep(2)
    
    def testSearchFlights(self, destination, date, returnDate):
        self.driver.find_element(*MainPageLocators.GoogleTravelDestination).send_keys(destination)
        sleep(2)
        self.driver.find_element(*MainPageLocators.GoogleTravelDestinationClick).click()
        sleep(2)
        self.driver.find_element(*MainPageLocators.GoogleTravelDeparture).send_keys(date)
        sleep(2)
        self.driver.find_element(*MainPageLocators.GoogleTravelReturn).click()
        self.driver.find_element(*MainPageLocators.GoogleTravelReturn).send_keys(returnDate)
        self.driver.find_element(*MainPageLocators.GoogleTravelReturn).send_keys(Keys.RETURN)
        sleep(2)
        self.driver.find_element(*MainPageLocators.GoogleTravelDateDoneButton).click()
        self.driver.find_element(*MainPageLocators.GoogleTravelSearchButton).click()
        sleep(10)

    def takeScreenShot(self):
        self.driver.save_screenshot('/Users/khallidwilliams/Downloads/FlightScreenShot.png')
        sleep(2)
        print("Screenshot taken")

    def testPurchseFlight(self):
        self.driver.find_element(*MainPageLocators.DepartFlight).click()
        sleep(2)
        self.driver.find_element(*MainPageLocators.ReturnFlight).click()
        sleep(2)
        self.driver.execute_script("window.scrollBy(0, 200);")
        print("Scrolled")
        sleep(2)
        self.driver.find_element(*MainPageLocators.ContinueButton).click()
        print("Navigated to Airlines webpage")

class NikeBot(BasePage):

    def searchNike(self, search):
        self.driver.find_element(*MainPageLocators.Nike_Search).click()
        sleep(2)
        self.driver.find_element(*MainPageLocators.Nike_Search_Bar).send_keys(search)
        self.driver.find_element(*MainPageLocators.Nike_Search_Bar).send_keys(Keys.RETURN)
        sleep(5)
    
    def selectNikeShoe(self):
        self.driver.find_element(*MainPageLocators.SelectNikeAirMaxPlusOG).click()
        sleep(5)

    def clickAirMaxButton(self):
        self.driver.find_element(*MainPageLocators.AirmaxPlusButton).click()
        sleep(3)
    
    def selectNikeSize(self):
        self.driver.find_element(*MainPageLocators.Nike_Size).click()
        sleep(2)
    
    def addToCart(self):
        self.driver.find_element(*MainPageLocators.Nike_Add_To_Cart).click()
        sleep(2)
        print("Added to cart")

    def exit_modal(self):
        self.driver.find_element(*MainPageLocators.Nike_Exit_Modal).click()
        sleep(2)
        print("Modal closed")