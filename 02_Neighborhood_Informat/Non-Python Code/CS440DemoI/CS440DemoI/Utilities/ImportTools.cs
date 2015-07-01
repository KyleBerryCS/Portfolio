using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS440DemoI.Utilities
{
    class ImportTools
    {
        // Because we are only importing and exporting community data... all we care about in the file is the community name on the first line
        // so let's get it from the file...

        public static int ImportSeachData()
        {
            // Configure open file dialog box
            Microsoft.Win32.OpenFileDialog dlg = new Microsoft.Win32.OpenFileDialog();
            dlg.FileName = "SearchData.txt"; // Default file name
            dlg.DefaultExt = ".txt"; // Default file extension
            dlg.Filter = "Text documents (.txt)|*.txt"; // Filter files by extension 

            // Show open file dialog box
            Nullable<bool> result = dlg.ShowDialog();

            // Process open file dialog box results 
            if (result == true)
            {
                // Open document 
                string filename = dlg.FileName;
                // Stream reader here...
                string line;
                string foundIndex;
                using (StreamReader sr = new StreamReader(filename))
                {
                    // Get the first line of the file...
                    line = sr.ReadLine();
                    Console.WriteLine("We found: " + line);
                    if (line.ElementAt(2) == ']')
                    {
                        foundIndex = line.Substring(1, 1);
                    }
                    else
                    {
                        // We must have a double digit index number...
                        foundIndex = line.Substring(1, 2);
                    }
                }
                Console.WriteLine("Found index: " + foundIndex);
                // Return the combobox index number in order to do the search.
                return Convert.ToInt32(foundIndex);
            }
            return -1;
        }
    }
}
