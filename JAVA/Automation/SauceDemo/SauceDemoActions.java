package SD;
import static org.testng.Assert.assertEquals;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import SauceDemoLocators;

public class SauceDemoActions {
    WebDriver driver;

    public SauceDemoActions(WebDriver driver) {
        this.driver = driver;
    }

    public void login(String name, String pass) {
        SauceDemoLocators locators = new SauceDemoLocators();
        driver.findElement(locators.username).click();
        driver.findElement(locators.username).sendKeys(name);

        driver.findElement(locators.password).click();
        driver.findElement(locators.password).sendKeys(pass);
    }

    public void clickLoginButton() {
        driver.find_element(locators.loginButton).click();
    }

    public void clickSauceLabsBackPack() {
        driver.find_element(locators.sauce_labs_backpack).click();
    }

    public void clickAddToCart() {
        driver.find_element(locators.add_to_card).click();
    }

    public void clickBackToProducts() {
        driver.find_element(locators.back_to_products).click();
    }

    public void add_tshirt_to_cart() {
        driver.find_element(locators.tshirt_add_to_card).click();
    }

    public void add_fleece_jacket_to_cart() {
        driver.find_element(locators.fleece_jacket_add_to_card).click();
    }

    public void click_cart() {
        driver.find_element(locators.cart).click();
    }

    public void click_checkout() {
        driver.find_element(locators.checkout_button).click();
    }

    public void fill_out_form(String firstname, String lastname, String zipcode) {
        driver.find_element(locators.first_name).click();
        driver.find_element(locators.first_name).sendKeys(firstname);

        driver.find_element(locators.last_name).click();
        driver.find_element(locators.last_name).sendKeys(lastname);

        driver.find_element(locators.zip).click();
        driver.find_element(locators.zip).sendKeys(zipcode);
    }

    public void continueButton() {
        driver.find_element(locators.continue_button).click();
    }

    public void finishButton() {
        driver.find_element(locators.finish_button).click();
    }

    public void backHomeButton() {
        driver.find_element(locators.back_home).click();
    }

    public void logout() {
        driver.find_element(locators.menu).click();
    }
}