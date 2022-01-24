using OpenQA.Selenium;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AHS_Automation.src.pages.PDF
{
    partial class PDFPage : BasePage
    {
        public bool IsPDFDisplayed()
        {
            return ProFaxReportID.Displayed;
        }
        public bool IsDentalBenefitsContractDisplayed()
        {
            return DentalBenefitsContract.Displayed;
        }     
    }
}
