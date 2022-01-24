using OpenQA.Selenium;
using OpenQA.Selenium.Appium;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AHS_Automation.src.pages
{
    partial class BasePage
    {
        private readonly IWebDriver driver;

        public BasePage(IWebDriver driver) => this.driver = driver;
    }
}
