using OpenQA.Selenium;
using OpenQA.Selenium.Appium.Windows;
using OpenQA.Selenium.Interactions;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AHS_Automation.src.pages.PDF
{
    partial class PDFPage : BasePage
    {
        private readonly IWebDriver webDriver;

        public PDFPage(IWebDriver webDriver) : base(webDriver) => this.webDriver = webDriver;

        public void SaveAsDocument(string value)
        {
            Actions action = new Actions(webDriver);
            action.ContextClick().Build().Perform();
            action.SendKeys(value).Build().Perform();
            action.SendKeys(Keys.Enter).Build().Perform();
        }
    }
}
