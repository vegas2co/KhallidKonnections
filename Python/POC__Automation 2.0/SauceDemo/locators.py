from selenium.webdriver.common.by import By

class SauceDemoLocators(object):

    #SauceDemo Login
    username = (By.XPATH, '//*[@id="user-name"]')
    password = (By.XPATH, '//*[@id="password"]')
    loginButton = (By.XPATH, '//*[@id="login-button"]')

    #Products
    header = (By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[2]/div')
    sauce_labs_backpack = (By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div')
    item_title = (By.XPATH, '/html/body/div/div/div/div[2]/div/div/div[2]/div[1]')
    add_to_card = (By.XPATH, '//*[@id="add-to-cart"]')
    back_to_products = (By.XPATH, '//*[@id="back-to-products"]')
    tshirt_add_to_card = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    fleece_jacket_add_to_card = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
    cart = (By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[3]/a')
    menu = (By.XPATH, '//*[@id="react-burger-menu-btn"]')
    logout_button = (By.XPATH, '//*[@id="react-burger-menu-btn"')

    #Cart
    checkout_button = (By.XPATH, '//*[@id="checkout"]')
    #Form
    first_name = (By.XPATH, '//*[@id="first-name"]')
    last_name = (By.XPATH, '//*[@id="last-name"]')
    zip = (By.XPATH, '//*[@id="postal-code"]')
    continue_button = (By.XPATH, '//*[@id="continue"]')
    finish_button = (By.XPATH, '//*[@id="finish"]')

    #Success
    success = (By.XPATH, '/html/body/div/div/div/div[2]/h2')
    back_home = (By.XPATH, '//*[@id="back-to-products"]')
