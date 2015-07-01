using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS440DemoI.Utilities
{
    class ExportTools
    {
        // Because we can only export for community data... that's all we care about
        public static string commName { get; set; }
        public static string comboIndex { get; set; }
        public static string perCapitaIncome { get; set; }
        public static string hardshipIndex { get; set; }
        private static string crimesName = "Crimes";
        public static string totalCommCrimes { get; set; }
        public static string totalChicagoAreaCrimes { get; set; }
        public static string commCrimePercentage { get; set; }
        public static IEnumerable<Database.CrimeType> crimes { get; set; }

        public static bool ExportData()
        {

            // Configure save file dialog box
            Microsoft.Win32.SaveFileDialog dlg = new Microsoft.Win32.SaveFileDialog();
            dlg.FileName = "SearchData"; // Default file name
            dlg.DefaultExt = ".txt"; // Default file extension
            dlg.Filter = "Text documents (.txt)|*.txt"; // Filter files by extension 

            // Show save file dialog box
            Nullable<bool> result = dlg.ShowDialog();

            // Process save file dialog box results 
            if (result == true)
            {
                // Save document 
                string filename = dlg.FileName;
                using (StreamWriter sw = new StreamWriter(filename))
                {
                    sw.WriteLine("[" + comboIndex + "] " + commName);
                    sw.WriteLine();
                    sw.WriteLine("\t" + perCapitaIncome);
                    sw.WriteLine("\t" + hardshipIndex);
                    sw.WriteLine("\t" + crimesName);

                    foreach (Database.CrimeType ct in crimes)
                    {
                        sw.WriteLine("\t\t" + ct.CrimeName + ": " + ct.CrimeCount.ToString() + " [" + ct.Percentage + "%]");
                    }
                }
                return true;
            }
            return false;
        }
    }
}
