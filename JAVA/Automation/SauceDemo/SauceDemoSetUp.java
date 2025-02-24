package SD;
import java.util. concurrent. TimeUnit;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import io.github.bonigarcia.wdm.WebDriverManager;

public class SauceDemoSetUp {
    String driverPath = "/Users/khallidwilliams/Desktop/Khallid Konnections/geckodriver";
    public static void main(String[] args) {
        WebDriverManager.FirefoxDriver().setup();

        // Create an instance of FirefoxDriver
        WebDriver driver = new FirefoxDriver();

        // Open a website
        driver.get("https://www.example.com");

        // Close the browser
        driver.quit();
    }
}