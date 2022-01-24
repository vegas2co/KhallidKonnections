using Allure.Commons;
using NUnit.Allure.Attributes;
using NUnit.Allure.Core;
using NUnit.Framework;
using OpenQA.Selenium;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using AHS_Automation.src.pages.google;

namespace AHS_Automation.src.Tests
{
    [TestFixture]
    [AllureNUnit]
    [AllureSuite("Google")]
    class GoogleTests : TestBase
    {
        public IWebDriver webDriver;

        [OneTimeSetUp]
        public void OneTimeSetup()
        {
            webDriver = InitializeChromeDriver();
        }

        [SetUp]
        public void SetUp()
        {
        }

        [OneTimeTearDown]
        public void OneTimeTearDown()
        {
            webDriver.Quit();
        }

        [AllureTag("Regression", "Needs Work", "Website", "IPLAN")]
        [AllureSubSuite("Batch 1")]
        [AllureSeverity(SeverityLevel.critical)]
        [AllureIssue("Age Selection page for Individual Plan resets DOB when user selects anywhere else on the page", "https://github.com/QualityLogic/AHS-Automation/issues/84")]
        [AllureIssue("Test is missing the insturctions for validating that enrollment worked")]
        [AllureLabel("Test Number", "330")]
        [Test]
        public void EnrollNewMemberAndDependentsInIndividualPlanTest()
        {
            IndividualPlanPage individualPlanPage = new IndividualPlanPage(webDriver);
            individualPlanPage.Visit();

            AgeSelectionPage ageSelectionPage = individualPlanPage.SelectBrowsePlansBtn();
            Assert.IsTrue(ageSelectionPage.IsDateOfBirthInputFieldDisplayed());
            Assert.IsTrue(ageSelectionPage.IsDateOfBirthInputFieldUsable());
            ageSelectionPage.SetDateOfBirthInputField("01011980");

            PlansPage plansPage = ageSelectionPage.SelectNextBtn();
            Assert.IsTrue(plansPage.IsEssentialPlanEnrollmentButtonDisplayed());

            EnrollPage enrollPage = plansPage.SelectPlan();
            Assert.IsTrue(enrollPage.IsFirstNameFieldDisplayed());
            enrollPage.SetFirstNameField("Automation");
            enrollPage.SetLastNameInputField("Automation");
            enrollPage.SetGenderDropdownField("Male");
            enrollPage.SetSSNInputField($"919{RandomizeSSN()}");

            enrollPage.SetMailingAddressInputField("123 Front St");
            enrollPage.SetCityDropdownField("Boise");
            enrollPage.SetZipCodeInputField("12345");
            enrollPage.SetPhoneNumberInputField("1235551234");
            enrollPage.SetEmailInputField("automation@deltadentalid.com");

            PaymentPage paymentPage = enrollPage.SelectContinueToPaymentBtn();
            Assert.True(paymentPage.IsNameOnCardInputFieldDisplayed());
            paymentPage.SetNameOnCardField("Automation");
            paymentPage.SetCardNumberField("4111111111111111");
            paymentPage.SetCardTypeDropdownField("VISA");
            paymentPage.SetExpirationMonthDropdownField("January");
            paymentPage.SetExpirationYearDropdownField("2022");

            ConfirmPage confirmPage = paymentPage.SelectContinueToConfirmationPageBtn();
            Assert.True(confirmPage.IsTermsCheckboxDisplayed());
            confirmPage.SelectTermsCheckbox();
            Assert.True(confirmPage.IsTermsCheckboxChecked());

            SuccessPage successPage = confirmPage.SelectFinishBtn();
            Assert.True(successPage.IsDeltaDentalHomeButtonDisplayed());

            //Validate that new user and dependents exist in individual plan subgroup
            Assert.Fail();
        }
    }
}
