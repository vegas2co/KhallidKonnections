import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.How;
import org.openqa.selenium.support.PageFactory;

public class SauceDemoLocators {

    WebDriver driver;

    // Constructor to initialize elements
    public SauceDemoLocators(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    // SauceDemo Login
    @FindBy(xpath = "//*[@id='user-name']")
    WebElement username;

    @FindBy(xpath = "//*[@id='password']")
    WebElement password;

    @FindBy(xpath = "//*[@id='login-button']")
    WebElement loginButton;

    // Products
    @FindBy(xpath = "/html/body/div/div/div/div[1]/div[1]/div[2]/div")
    WebElement header;

    @FindBy(xpath = "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a/div")
    WebElement sauce_labs_backpack;

    @FindBy(xpath = "/html/body/div/div/div/div[2]/div/div/div[2]/div[1]")
    WebElement item_title;

    @FindBy(xpath = "//*[@id='add-to-cart']")
    WebElement add_to_cart;

    @FindBy(xpath = "//*[@id='back-to-products']")
    WebElement back_to_products;

    @FindBy(xpath = "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    WebElement tshirt_add_to_cart;

    @FindBy(xpath = "//*[@id='add-to-cart-sauce-labs-fleece-jacket']")
    WebElement fleece_jacket_add_to_cart;

    @FindBy(xpath = "/html/body/div/div/div/div[1]/div[1]/div[3]/a")
    WebElement cart;

    @FindBy(xpath = "//*[@id='react-burger-menu-btn']")
    WebElement menu;

    @FindBy(xpath = "//*[@id='logout_sidebar_link']")
    WebElement logout_button; // Updated locator for logout button

    // Cart
    @FindBy(xpath = "//*[@id='checkout']")
    WebElement checkout_button;

    // Form
    @FindBy(xpath = "//*[@id='first-name']")
    WebElement first_name;

    @FindBy(xpath = "//*[@id='last-name']")
    WebElement last_name;

    @FindBy(xpath = "//*[@id='postal-code']")
    WebElement zip;

    @FindBy(xpath = "//*[@id='continue']")
    WebElement continue_button;

    @FindBy(xpath = "//*[@id='finish']")
    WebElement finish_button;

    // Success
    @FindBy(xpath = "/html/body/div/div/div/div[2]/h2")
    WebElement success;

    @FindBy(xpath = "//*[@id='back-to-products']")
    WebElement back_home;
}
