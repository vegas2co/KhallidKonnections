import static org.testng.Assert.assertEquals;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import SauceDemoLocators.*;

public class SauceDemoActions {
    WebDriver driver;
    SauceDemoLocators locators = new SauceDemoLocators(driver);

    public SauceDemoActions(WebDriver driver) {
        this.driver = driver;

    }

    public void login(String name, String pass) {
        locators.username.click();
        locators.username.sendKeys(name);

        locators.password.click();
        locators.password.sendKeys(pass);
    }

    public void clickLoginButton() {
        locators.loginButton.click();
    }

    public void clickSauceLabsBackPack() {
        locators.sauce_labs_backpack.click();
    }

    public void clickAddToCart() {
        locators.add_to_cart.click();
    }

    public void clickBackToProducts() {
        locators.back_to_products.click();
    }

    public void add_tshirt_to_cart() {
        locators.tshirt_add_to_cart.click();
    }

    public void add_fleece_jacket_to_cart() {
        locators.fleece_jacket_add_to_cart.click();
    }

    public void click_cart() {
        locators.cart.click();
    }

    public void click_checkout() {
        locators.checkout_button.click();
    }

    public void fill_out_form(String firstname, String lastname, String zipcode) {
        locators.first_name.click();
        locators.first_name.sendKeys(firstname);

        locators.last_name.click();
        locators.last_name.sendKeys(lastname);

        locators.zip.click();
        locators.zip.sendKeys(zipcode);
    }

    public void continueButton() {
        locators.continue_button.click();
    }

    public void finishButton() {
        locators.finish_button.click();
    }

    public void backHomeButton() {
        locators.back_home.click();
    }

    public void logout() {
        locators.menu.click();
    }
}