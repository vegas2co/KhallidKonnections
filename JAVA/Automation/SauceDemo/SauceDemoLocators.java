public class SauceDemoLocators {

    WebDriver driver;

    //SauceDemo Login
    @FindBy(XPATH = "//*[@id='user-name']") WebElement username;
    @FindBy(XPATH = "//*[@id='password']") WebElement password;
    @FindBy(XPATH = "//*[@id='login-button']") WebElement loginButton;

    //Products
    @FindBy(XPATH = "/html/body/div/div/div/div[1]/div[1]/div[2]/div]") WebElement header;
    @FindBy(XPATH = "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div") WebElement sauce_labs_backpack;
    @FindBy(XPATH = "/html/body/div/div/div/div[2]/div/div/div[2]/div[1]") WebElement item_title;
    @FindBy(XPATH = "//*[@id='add-to-cart']") WebElement add_to_card;
    @FindBy(XPATH = "//*[@id='back-to-products']") WebElement back_to_products;
    @FindBy(XPATH = "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']") WebElement tshirt_add_to_card;
    @FindBy(XPATH = "//*[@id='add-to-cart-sauce-labs-fleece-jacket']") WebElement fleece_jacket_add_to_card;
    @FindBy(XPATH = "/html/body/div/div/div/div[1]/div[1]/div[3]/a") WebElement cart;
    @FindBy(XPATH = "//*[@id='react-burger-menu-btn']") WebElement menu;
    @FindBy(XPATH = "//*[@id='react-burger-menu-btn'") WebElement logout_button;

    //Cart
    @FindBy(XPATH = "//*[@id='checkout']") WebElement checkout_button;

    //Form
    @FindBy(XPATH = "//*[@id='first-name']") WebElement first_name;
    @FindBy(XPATH = "//*[@id='last-name']") WebElement last_name;
    @FindBy(XPATH = "//*[@id='postal-code']") WebElement zip;
    @FindBy(XPATH = "//*[@id='continue']") WebElement continue_button;
    @FindBy(XPATH = "//*[@id='finish']") WebElement finish_button;

    //Success
    @FindBy(XPATH = "/html/body/div/div/div/div[2]/h2") WebElement success;
    @FindBy(XPATH = "//*[@id='back-to-products']") WebElement back_home;
}