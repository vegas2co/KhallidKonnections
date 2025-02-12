from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""

    #PYTHON
    GO_BUTTON = (By.ID, 'submit')
    SEARCH_BOX = (By.ID, 'id-search-field')

    #GOOGLE
    KhallidKonnectionsLink = (By.CSS_SELECTOR, '#rso > div:nth-child(2) > div > div:nth-child(1) > div > div > div.NJo7tc.Z26q7c.jGGQ5e > div > a > h3')
    
    #YOUTUBE
    YouTube_Search_Button = (By.XPATH, '/html/body/ytd-app/div[1]/div[2]/ytd-masthead/div[4]/div[2]/yt-searchbox/button')
    Click_KK_Video = (By.LINK_TEXT, 'Khallid Konnect')
    Full_Screen_Video = (By.CSS_SELECTOR, '#c4-player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button.ytp-fullscreen-button.ytp-button')

    #YAHOO
    Yahoo_Signin = (By.XPATH, '/html/body/div[1]/a')
    Yahoo_Username = (By.XPATH, '//*[@id="login-username"]')
    Yahoo_Next_Button = (By.XPATH, '//*[@id="login-signin"]')
    Yahoo_Password = (By.XPATH, '//*[@id="login-passwd"]')
    Yahoo_Confirm_Signin = (By.XPATH, '//*[@id="login-signin"]')
    Yahoo_SearchBox = (By.XPATH, '/html/body/header/div/div/div[3]/div/div[2]/div/div/div/div[1]/ul/li/div/div/input[1]')

    #QADEMO
    QADemo_FirstName = (By.XPATH, '//*[@id="firstName"]')
    QADemo_LastName = (By.XPATH, '//*[@id="lastName"]')
    QADemo_Email = (By.XPATH, '//*[@id="userEmail"]')
    QADemo_Phone = (By.XPATH, '//*[@id="userNumber"]')
    QADemo_Subject = (By.XPATH, '//*[@id="subjectsInput"]')
    QADemo_Address = (By.XPATH, '//*[@id="currentAddress"]')
    QADemo_submitButton = (By.XPATH, '//*[@id="submit"]')

    #Bing   
    Bing_Search = (By.XPATH, '//*[@id="sb_form_q"]')

    #Google Travel
    GoogleTravelOrigin = (By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div/input')
    GoogleTravelDestination = (By.CSS_SELECTOR, '#i23 > div.e5F5td.vxNK6d > div > div > div.cQnuXe.k0gFV > div > div > input')
    GoogleTravelDestinationClick = (By.CLASS_NAME, 'CwL3Ec')
    GoogleTravelDeparture = (By.CSS_SELECTOR, 'body > c-wiz.zQTmif.SSPGKf > div > div:nth-child(2) > c-wiz > div.cKvRXe > c-wiz > div.vg4Z0e > div:nth-child(1) > div.SS6Dqf.POQx1c > div.AJxgH > div > div.rIZzse > div.bgJkKe.K0Tsu > div > div > div.cQnuXe.k0gFV > div > div > div:nth-child(1) > div > div.GYgkab.YICvqf.kStSsc.ieVaIb > div > input')
    GoogleTravelReturn = (By.CSS_SELECTOR, 'body > c-wiz.zQTmif.SSPGKf > div > div:nth-child(2) > c-wiz > div.cKvRXe > c-wiz > div.vg4Z0e > div:nth-child(1) > div.SS6Dqf.POQx1c > div.AJxgH > div > div.rIZzse > div.bgJkKe.K0Tsu > div > div > div.cQnuXe.k0gFV > div > div > div:nth-child(1) > div > div.GYgkab.YICvqf.lJODHb.qXDC9e > div > input')
    GoogleTravelDateDoneButton = (By.CSS_SELECTOR, 'button.DuMIQc:nth-child(1) > span:nth-child(4)')
    GoogleTravelSearchButton = (By.CSS_SELECTOR, 'body > c-wiz.zQTmif.SSPGKf > div > div:nth-child(2) > c-wiz > div.cKvRXe > c-wiz > div.vg4Z0e > div:nth-child(1) > div.SS6Dqf.POQx1c > div.MXvFbd > div > button')

    DepartFlight = (By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/div/div[2]/div[1]/ul/li[1]/div/div[2]')  
    ReturnFlight = (By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]')
    ContinueButton = (By.CSS_SELECTOR, '.DuMIQc')

    TopFlightsText = (By.CSS_SELECTOR, '.eQ35Ce > div:nth-child(2) > div:nth-child(1) > h3:nth-child(1)')

    #Google Travel Assert
    DepartFlightList = (By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/div/div[2]/div[1]/ul')
    DepartFlightTime = (By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/div/div[2]/div[1]/ul/li[1]/div/div[2]/div/div[2]/div/div[2]/div[1]')
    DepartFlightLength = (By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/div/div[2]/div[1]/ul/li[1]/div/div[2]/div/div[2]/div/div[3]/div')
    DepartNonStops = (By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/div/div[2]/div[1]/ul/li[2]/div/div[2]/div/div[2]/div/div[4]/div[1]/span')
    DepartFlightPrice = (By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/div/div[2]/div[1]/ul/li[1]/div/div[2]/div/div[2]/div/div[6]/div[1]/div[2]/span')

    ReturnFlightList = (By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul')
    ReturnFlightTime = (By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/span')
    ReturnFlightLength = (By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div/div[3]/div')
    ReturnNonStops = (By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div/div[4]/div[1]/span')
    ReturnFlightPrice = (By.XPATH, '/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[3]/ul/li[1]/div/div[2]/div/div[2]/div/div[6]/div[1]/div[2]/span')

    #NIKE
    Nike_Search = (By.XPATH, '//*[@id="nav-search-icon"]')
    Nike_Search_Bar = (By.XPATH, '//*[@id="gn-search-input"]')
    Nike_Size = (By.XPATH, '/html/body/div[5]/div/main/div[2]/div[3]/div[3]/fieldset/div[1]/div/div[11]') 
    Nike_Add_To_Cart = (By.XPATH, '/html/body/div[5]/div/main/div[2]/div[3]/div[5]/div[1]/button')

    AirmaxPlusButton = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div[4]/div/div[5]/div[1]/div[1]/div[2]/div/div/div/div/nav/div[2]/div/div/button[9]')
    SelectNikeAirMaxPlusOG = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div[4]/div/div[5]/div[2]/main/section/div/div[1]/div/figure/a[2]/div/img')
    Nike_Shoe_Name = (By.XPATH, '//*[@id="pdp_product_title"]')
    
    #Nike Modal
    Nike_Error_Message_Modal = (By.XPATH, '/html/body/div[10]/div/div/div/div/div/div/div/div')
    Nike_Error_Message_Modal_Title = (By.XPATH, '/html/body/div[10]/div/div/div/div/div/div/div/div/h2')
    Nike_Error_Message_Modal_Text = (By.XPATH, '/html/body/div[10]/div/div/div/div/div/div/div/div/p[1]')
    Nike_Exit_Modal = (By.XPATH, '/html/body/div[10]/div/div/div/div/div/div/div/button')

    Nike_Search_Results = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div[4]/div/div[3]/header/div/h1/span[1]')
    Nike_Search_Name = (By.XPATH, '/html/body/div[4]/div/div/div[2]/div[4]/div/div[3]/header/div/h1/span[2]')

    #American Airlines
    From_input_box = (By.XPATH, '//*[@id="reservationFlightSearchForm.originAirport"]')
    To_input_box = (By.XPATH, '//*[@id="reservationFlightSearchForm.destinationAirport"]')
    Departure_date = (By.XPATH, '//*[@id="aa-leavingOn"]')
    Return_date = (By.XPATH, '//*[@id="aa-returningFrom"]')
    Search_Button = (By.XPATH, '//*[@id="flightSearchForm.button.reSubmit"]')

    #American Airlines assertions
    booking_modal = (By.CSS_SELECTOR, "#booking-module-tabs")
    Privacy_cookies_popup_modal = (By.ID, 'cookie-banner')
    Privacy_cookies_popup_dismiss = (By.ID, 'button')

    departing_flights_header = (By.XPATH, '//*[@id="header"]')
    returning_flights_header = (By.XPATH, '/html/body/app-root/app-results/main/div/div[1]/div[1]/h1/span[1]')
    choose_flight = (By.XPATH, '//*[@id="flight-1-product-group-MAIN"]')
    select_flight = (By.XPATH, '//*[@id="slice-1-MAIN-coach"]')
    choose_return_flight = (By.XPATH, '//*[@id="flight-2-product-group-MAIN"]')
    select_return_flight = (By.XPATH, '//*[@id="slice-2-MAIN-coach"]')

    Upgrade_to_main_plus_modal = (By.XPATH, '//*[@id="cdk-overlay-1"]')
    Upgrade_to_main_plus_modal_exit = (By.XPATH, '/html/body/div[1]/div[2]/div/mat-dialog-container/div/div/app-main-cabin-upsell-desktop/div/div[1]/div[1]/button')
    continue_as_guest_button = (By.XPATH, '//*[@id="continue-as-guest-btn"]')
    loginIn_button = (By.XPATH, '//*[@id="login-continue-btn"]')

    firstName = (By.XPATH, '//*[@id="passengers0.personalInformationForm.firstName"]')
    lastName = (By.XPATH, '//*[@id="passengers0.personalInformationForm.lastName"]')
    month_dropbox = (By.XPATH, '//*[@id="passengers0.dateComponentForm.month"]')
    day_dropbox = (By.XPATH, '//*[@id="passengers0.dateComponentForm.day"]')
    year_dropbox = (By.XPATH, '//*[@id="passengers0.dateComponentForm.year"]')
    gender_dropbox = (By.XPATH, '//*[@id="passengers0.personalInformationForm.gender"]')
    country_dropbox = (By.XPATH, '//*[@id="passengers0.residencyInfo.country"]')
    state_dropbox = (By.XPATH, '//*[@id="passengers0.residencyInfo.state"]')
    primary_email = (By.XPATH, '//*[@id="tripContact.email"]')
    confirm_primary_email = (By.XPATH, '//*[@id="confirmEmail"]')
    phoneNumber_dropbox = (By.XPATH, '//*[@id="tripContact.phones0.type"]')
    phoneNumber_textbox = (By.XPATH, '//*[@id="phoneNumber"]')
    continue_button = (By.XPATH, '//*[@id="passenger_button"]')