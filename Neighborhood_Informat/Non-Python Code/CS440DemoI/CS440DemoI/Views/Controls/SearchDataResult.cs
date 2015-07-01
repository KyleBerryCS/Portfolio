using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace CS440DemoI.Views.Controls
{
    class SearchDataResult
    {
        private Border outerBorder = new Border();
        private StackPanel dataStackPanel = new StackPanel();
        private Label NameLabel = new Label();
        private Label crimesLabel = new Label();
        private Label crimeInfoLabel1 = new Label();
        private Label crimeInfoLabel2 = new Label();
        private Label crimeInfoLabel3 = new Label();
        private Label crimeInfoLabel4 = new Label();
        private Label perCapTitle = new Label();
        private Label hardshipTitle = new Label();
        private Label tifTitle = new Label();

        public SearchDataResult(string Name, IEnumerable<Database.CrimeType> Crimes, IEnumerable<int?> PerCapitaIncome, IEnumerable<int?> HardshipIndex)
        {
            this.outerBorder.BorderBrush = Brushes.Black;
            this.outerBorder.BorderThickness = new Thickness(1.0);
            this.outerBorder.Width = 1200;

            this.NameLabel.Content = Name;
            Utilities.ExportTools.commName = Name;
            this.NameLabel.FontSize = 24.0;
            this.dataStackPanel.Children.Add(this.NameLabel);

            this.perCapTitle.Content = "Per Capita Income: $" + PerCapitaIncome.First().ToString() + ".00";
            Utilities.ExportTools.perCapitaIncome = "Per Capita Income: $" + PerCapitaIncome.First().ToString() + ".00";
            this.perCapTitle.FontSize = 16.0;
            this.dataStackPanel.Children.Add(this.perCapTitle);

            this.hardshipTitle.Content = "Hardship Index: " + HardshipIndex.First().ToString();
            Utilities.ExportTools.hardshipIndex = "Hardship Index: " + HardshipIndex.First().ToString();
            this.hardshipTitle.FontSize = 16.0;
            this.dataStackPanel.Children.Add(this.hardshipTitle);

            this.tifTitle.Content = "Tax Increment Financing (TIF): ";
            if (NIKernel.Instance.SearchPageView.BlockRadio.IsChecked == true)
            {
                this.tifTitle.Content += "Block returned content here";
            }
            else
            {
                this.tifTitle.Content += "Only available in search by block";
            }
            this.tifTitle.FontSize = 16.0;
            this.dataStackPanel.Children.Add(this.tifTitle);

            this.crimesLabel.Content = "Crimes";
            this.crimesLabel.FontSize = 16.0;
            this.dataStackPanel.Children.Add(this.crimesLabel);
            Database.CrimeType ctInfo = Crimes.First();
            this.crimeInfoLabel1.Content = "Total community crimes: " + ctInfo.TotalCommCrimes.ToString();
            Utilities.ExportTools.totalCommCrimes = "Total community crimes: " + ctInfo.TotalCommCrimes.ToString();
            this.crimeInfoLabel1.Margin = new Thickness(30, 0, 0, 0);
            this.crimeInfoLabel1.FontSize = 14;
            this.dataStackPanel.Children.Add(this.crimeInfoLabel1);
            this.crimeInfoLabel2.Content = "Total Chicago area crimes: " + ctInfo.TotalCrimes.ToString();
            Utilities.ExportTools.totalChicagoAreaCrimes = "Total Chicago area crimes: " + ctInfo.TotalCrimes.ToString();
            this.crimeInfoLabel2.Margin = new Thickness(30, 0, 0, 0);
            this.crimeInfoLabel2.FontSize = 14;
            this.dataStackPanel.Children.Add(this.crimeInfoLabel2);
            this.crimeInfoLabel3.Content = "Total community crime percentge of all crimes in Chicago: " + ctInfo.TotalCrimePercentage.ToString() + "%";
            Utilities.ExportTools.commCrimePercentage = "Total community crime percentge of all crimes in Chicago: " + ctInfo.TotalCrimePercentage.ToString() + "%";
            this.crimeInfoLabel3.Margin = new Thickness(30, 0, 0, 0);
            this.crimeInfoLabel3.FontSize = 14;
            this.dataStackPanel.Children.Add(this.crimeInfoLabel3);
            this.crimeInfoLabel4.Content = "Crime type breakdown (by type of crime): {[NAME]: No. of crimes [Percentage of crime type in community]}:";
            this.crimeInfoLabel4.Margin = new Thickness(30, 0, 0, 0);
            this.crimeInfoLabel4.FontSize = 14;
            this.dataStackPanel.Children.Add(this.crimeInfoLabel4);
            foreach (Database.CrimeType ct in Crimes)
            {
                Label ctLabel = new Label();
                ctLabel.Margin = new Thickness(60, 0, 0, 0);
                ctLabel.Content = ct.CrimeName + ": " + ct.CrimeCount.ToString() + " [" + ct.Percentage + "%]";
                this.dataStackPanel.Children.Add(ctLabel);
            }
            Utilities.ExportTools.crimes = Crimes;

            this.outerBorder.Child = this.dataStackPanel;
        }

        public Border GetDataControl()
        {
            return this.outerBorder;
        }
    }
}
