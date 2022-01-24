using OpenQA.Selenium;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AHS_Automation.src.pages.claims
{
    partial class ClaimsPage : BasePage
    {
        //Button
        private IWebElement ExportToPDF => driver.FindElement(By.Id("ctl00_MainContent_RailMemberClaimList_aspxGridViewClaimList_DXCTMenu0_DXI0_T"));
        private IWebElement ExportToXLS => driver.FindElement(By.Id("ctl00_MainContent_RailMemberClaimList_aspxGridViewClaimList_DXCTMenu0_DXI1_T"));
        private IWebElement ExportToXLSX => driver.FindElement(By.Id("ctl00_MainContent_RailMemberClaimList_aspxGridViewClaimList_DXCTMenu0_DXI2_T"));
        private IWebElement ExportToDOCX => driver.FindElement(By.Id("ctl00_MainContent_RailMemberClaimList_aspxGridViewClaimList_DXCTMenu0_DXI3_T"));
        private IWebElement ExportToRTF => driver.FindElement(By.Id("ctl00_MainContent_RailMemberClaimList_aspxGridViewClaimList_DXCTMenu0_DXI4_T"));
        private IWebElement ExportToCSV => driver.FindElement(By.Id("ctl00_MainContent_RailMemberClaimList_aspxGridViewClaimList_DXCTMenu0_DXI5_T"));
        //Input Field
        private IWebElement SearchBox => driver.FindElement(By.Id("ctl00_MainContent_RailMemberClaimList_aspxGridViewClaimList_DXSE_I"));
    }
}