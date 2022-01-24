using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AHS_Automation.src.pages.google
{
    partial class GooglePage : BasePage
    {
        public bool IsExportToPDFDisplayed()
        {
            return ExportToPDF.Displayed;
        }

        public bool IsExportToXLSDisplayed()
        {
            return ExportToXLS.Displayed;
        }

        public bool IsExportToXLSXDisplayed()
        {
            return ExportToXLSX.Displayed;
        }

        public bool IsExportToDOCXDisplayed()
        {
            return ExportToDOCX.Displayed;
        }

        public bool IsExportToRTFDisplayed()
        {
            return ExportToRTF.Displayed;
        }

        public bool IsExportToCSVDisplayed()
        {
            return ExportToCSV.Displayed;
        }

        public bool IsSearchBoxDisplayed()
        {
            return SearchBox.Displayed;
        }
        
    }
}