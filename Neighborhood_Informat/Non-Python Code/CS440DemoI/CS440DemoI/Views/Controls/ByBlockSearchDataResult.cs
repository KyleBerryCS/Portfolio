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
    class ByBlockSearchDataResult
    {
        private Border outerBorder = new Border();
        private StackPanel dataStackPanel = new StackPanel();
        private Label NameLabel = new Label();
        private Label tifLabel = new Label();
        private Label tifInfoLabel1 = new Label();

        public ByBlockSearchDataResult(string Name, decimal? TIF)
        {
            this.outerBorder.BorderBrush = Brushes.Black;
            this.outerBorder.BorderThickness = new Thickness(1.0);
            this.outerBorder.Width = 1200;

            this.NameLabel.Content = Name;
            this.NameLabel.FontSize = 24.0;
            this.dataStackPanel.Children.Add(this.NameLabel);

            this.tifLabel.Content = "Tax Increment Financing";
            this.tifLabel.FontSize = 16.0;
            this.dataStackPanel.Children.Add(this.tifLabel);
            this.tifInfoLabel1.Content = "Beginning of year amount: $" + TIF.ToString() + ".00";
            this.tifInfoLabel1.Margin = new Thickness(30, 0, 0, 0);
            this.tifInfoLabel1.FontSize = 14;
            this.dataStackPanel.Children.Add(this.tifInfoLabel1);

            this.outerBorder.Child = this.dataStackPanel;
        }

        public Border GetDataControl()
        {
            return this.outerBorder;
        }
    }
}
