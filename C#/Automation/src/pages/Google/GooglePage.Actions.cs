using OpenQA.Selenium;
using OpenQA.Selenium.Appium;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AHS_Automation.src.pages.google
{
    partial class GooglePage : BasePage
    {
        private readonly IWebDriver driver;

        public GooglePage(IWebDriver driver) : base(driver) => this.driver = driver;

    }
}