import static org.testng.Assert.assertEquals;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import SauceDemoLocators.*;

public class SauceDemoAssertions {
    //Home page action methods come here SauceDemo

    public SauceDemoAssertions(WebDriver driver) {
        this.driver = driver;
    }

    public void is_title_matches(String header_text) {
        String header = driver.find_element(locators.header).text;
        assertEquals(header, header_text);
    }

    public void is_item_title_matches(String item_text) {
        var header = driver.find_element(locators.item_title).text;
        assertEquals(header, item_text);
    }

    public void is_purchase_success(String success_message) {
        var header = driver.find_element(locators.success).text;
        assertEquals(header, success_message);
    }
}