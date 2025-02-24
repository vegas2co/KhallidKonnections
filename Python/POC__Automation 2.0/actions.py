from elements import BasePageElement
from locators import MainPageLocators
from locators import AmericanAirlinesPageLocators
from selenium.webdriver.common.keys import Keys
from time import sleep
import assertions
from selenium.webdriver.support.ui import Select
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

    def scroll(self, Y):
        self.driver.execute_script("window.scrollTo(0, "+str(Y)+")")
        sleep(2)

    def takeScreenShot(self, name):
        self.driver.save_screenshot('/Users/khallidwilliams/Downloads/'+ name +'.png')
        sleep(2)
        print("Screenshot taken")

    def navigateTo(self, url):
        self.driver.get(url)
        sleep(2)

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
    
    def openNewTab(self,tab_num):
        self.driver.execute_script("window.open('');") #open tab
        self.driver.switch_to.window(self.driver.window_handles[tab_num]) #switch to tab
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

    def testDepartFlight(self):
        self.driver.find_element(*MainPageLocators.DepartFlight).click()
        sleep(2)
    
    def testReturnFlight(self):
        self.driver.find_element(*MainPageLocators.ReturnFlight).click()
        sleep(2)
    
    def clickContinueButton(self):
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

class AmericanAirlinesBot(BasePage):
    def enter_flight_info(self,departFlight,returnFlight,depateDate,returnDate):
        self.driver.find_element(*AmericanAirlinesPageLocators.From_input_box).click()
        self.driver.find_element(*AmericanAirlinesPageLocators.From_input_box).send_keys(Keys.COMMAND, "a")
        self.driver.find_element(*AmericanAirlinesPageLocators.From_input_box).send_keys(departFlight)
        self.driver.find_element(*AmericanAirlinesPageLocators.To_input_box).send_keys(returnFlight)
        self.driver.find_element(*AmericanAirlinesPageLocators.Departure_date).send_keys(depateDate)
        self.driver.find_element(*AmericanAirlinesPageLocators.Return_date).send_keys(returnDate)

    def submit_flight(self):
        self.driver.find_element(*AmericanAirlinesPageLocators.Search_Button).click()

    def choose_departing_flight(self):
        self.driver.find_element(*AmericanAirlinesPageLocators.choose_flight).click()

    def select_departing_flight(self):
        self.driver.find_element(*AmericanAirlinesPageLocators.select_flight).click()

    def choose_returning_flgihts(self):
        self.driver.find_element(*AmericanAirlinesPageLocators.choose_return_flight).click()

    def select_returning_flight(self):
        self.driver.find_element(*AmericanAirlinesPageLocators.select_return_flight).click()

    def click_upgrade_to_main_plus_modal_exit(self):
        self.driver.find_element(*AmericanAirlinesPageLocators.Upgrade_to_main_plus_modal_exit).click()

    def click_continue_as_guess_button(self):
        self.driver.find_element(*AmericanAirlinesPageLocators.continue_as_guest_button).click()

    def enter_first_name(self,name):
        self.driver.find_element(*AmericanAirlinesPageLocators.firstName).click()
        self.driver.find_element(*AmericanAirlinesPageLocators.firstName).send_keys(name)


    def enter_last_name(self,name):
        self.driver.find_element(*AmericanAirlinesPageLocators.lastName).click()
        self.driver.find_element(*AmericanAirlinesPageLocators.lastName).send_keys(name)

    def click_month(self, index):
        month = self.driver.find_element(*AmericanAirlinesPageLocators.month_dropbox)
        self.driver.find_element(*AmericanAirlinesPageLocators.month_dropbox).click()
        select = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((month))))
        select.select_by_index(index)

    def click_day(self, index):
        day = self.driver.find_element(*AmericanAirlinesPageLocators.day_dropbox)
        self.driver.find_element(*AmericanAirlinesPageLocators.day_dropbox).click()
        select = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((day))))
        select.select_by_index(index)

    def click_year(self, index):
        year = self.driver.find_element(*AmericanAirlinesPageLocators.year_dropbox)
        self.driver.find_element(*AmericanAirlinesPageLocators.year_dropbox).click()
        select = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((year))))
        select.select_by_index(index)

    def click_gender(self, index):
        gender = self.driver.find_element(*AmericanAirlinesPageLocators.gender_dropbox)
        self.driver.find_element(*AmericanAirlinesPageLocators.gender_dropbox).click()
        select = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((gender))))
        select.select_by_index(index)

    def click_country(self, index):
        country = self.driver.find_element(*AmericanAirlinesPageLocators.country_dropbox)
        self.driver.find_element(*AmericanAirlinesPageLocators.country_dropbox).click()
        select = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((country))))
        select.select_by_index(index)

    def click_state(self, index):
        state = self.driver.find_element(*AmericanAirlinesPageLocators.state_dropbox)
        self.driver.find_element(*AmericanAirlinesPageLocators.state_dropbox).click()
        select = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((state))))
        select.select_by_index(index)

    def enter_email(self, email):
        self.driver.find_element(*AmericanAirlinesPageLocators.primary_email).click()
        self.driver.find_element(*AmericanAirlinesPageLocators.primary_email).send_keys(email)

    def enter_confirm_email(self, email):
        self.driver.find_element(*AmericanAirlinesPageLocators.confirm_primary_email).click()
        self.driver.find_element(*AmericanAirlinesPageLocators.confirm_primary_email).send_keys(email)
    
    def click_primary_phone_dropdown(self, index):
        phoneNumber = self.driver.find_element(*AmericanAirlinesPageLocators.phoneNumber_dropbox)
        self.driver.find_element(*AmericanAirlinesPageLocators.phoneNumber_dropbox).click()
        select = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((phoneNumber))))
        select.select_by_index(index)

    def enter_primary_phone(self, phoneNumber):
        self.driver.find_element(*AmericanAirlinesPageLocators.phoneNumber_textbox).click()
        self.driver.find_element(*AmericanAirlinesPageLocators.phoneNumber_textbox).send_keys(phoneNumber)

    def click_continue_button(self):
        self.driver.find_element(*AmericanAirlinesPageLocators.continue_button).click()

    def click_skip_seats_button(self):
        self.driver.find_element(*AmericanAirlinesPageLocators.skip_seats).click()

    def click_credit_debit_card_radio_button(self):
        self.driver.find_element(*AmericanAirlinesPageLocators.credit_debit_card_radio_button).click()

    def fill_out_credit_card_info(self,firstname,lastname,cardNumber,expire,address,city,state,index,zip):
        print('Started card details')
        self.driver.find_element(*AmericanAirlinesPageLocators.credit_card_first_name).click()
        self.driver.find_element(*AmericanAirlinesPageLocators.credit_card_first_name).send_keys(firstname)

        self.driver.find_element(*AmericanAirlinesPageLocators.credit_card_last_name).click()
        self.driver.find_element(*AmericanAirlinesPageLocators.credit_card_last_name).send_keys(lastname)

        self.driver.find_element(*AmericanAirlinesPageLocators.credit_card_card_number).click()
        self.driver.find_element(*AmericanAirlinesPageLocators.credit_card_card_number).send_keys(cardNumber)

        self.driver.find_element(*AmericanAirlinesPageLocators.credit_card_expiration).click()
        self.driver.find_element(*AmericanAirlinesPageLocators.credit_card_expiration).send_keys(expire)

        self.driver.find_element(*AmericanAirlinesPageLocators.credit_card_billing_address).click()
        self.driver.find_element(*AmericanAirlinesPageLocators.credit_card_billing_address).send_keys(address)

        self.driver.find_element(*AmericanAirlinesPageLocators.credit_card_city).click()
        self.driver.find_element(*AmericanAirlinesPageLocators.credit_card_city).send_keys(city)

        creditcard_dopdown = self.driver.find_element(*AmericanAirlinesPageLocators.credit_card_state)
        self.driver.find_element(*AmericanAirlinesPageLocators.credit_card_state).click()
        self.driver.find_element(*AmericanAirlinesPageLocators.credit_card_state).send_keys(state)
        select = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((creditcard_dopdown))))
        select.select_by_index(index)

        self.driver.find_element(*AmericanAirlinesPageLocators.credit_card_zipcode).click()
        self.driver.find_element(*AmericanAirlinesPageLocators.credit_card_zipcode).send_keys(zip)

    def click_terms_and_conditons(self):
        self.driver.find_element(*AmericanAirlinesPageLocators.terms_and_conditons).click()

    def click_pay_now_button(self):
        self.driver.find_element(*AmericanAirlinesPageLocators.paynow_button).click()