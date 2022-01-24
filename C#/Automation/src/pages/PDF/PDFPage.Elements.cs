using OpenQA.Selenium;
using OpenQA.Selenium.Appium.Windows;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AHS_Automation.src.pages.PDF
{
    partial class PDFPage : BasePage
    {
        private IWebElement ProFaxReportID => webDriver.FindElement(By.LinkText("Benefits & Eligibility"));
        private IWebElement DentalBenefitsContract => webDriver.FindElement(By.LinkText("Dental Benefits Contract"));

    }
}
