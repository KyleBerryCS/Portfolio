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
    class StatSearchResult
    {
        private Border outerBorder = new Border();
        private StackPanel dataStackPanel = new StackPanel();
        private Label NameLabel = new Label();
        private Label dataLabelTitle = new Label();
        private Label dataLabel = new Label();

        public StatSearchResult(string Name, string Title, string Value)
        {
            this.outerBorder.BorderBrush = Brushes.Black;
            this.outerBorder.BorderThickness = new Thickness(1.0);
            this.outerBorder.Width = 1200;

            this.NameLabel.Content = Name;
            this.NameLabel.FontSize = 24.0;
            this.dataStackPanel.Children.Add(this.NameLabel);

            this.dataLabelTitle.Content = Title + ": " + Value;
            this.dataLabelTitle.FontSize = 16.0;
            this.dataStackPanel.Children.Add(this.dataLabelTitle);

            this.outerBorder.Child = this.dataStackPanel;
        }

        public Border GetDataControl()
        {
            return this.outerBorder;
        }
    }
}
