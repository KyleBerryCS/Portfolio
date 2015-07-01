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
    class HotKeyControl
    {
        private Grid grid;
        private Label label;
        public Label HKLabel
        {
            get { return this.label; }
        }
        private ComboBox comboBox;
        private TextBox textBox;

        public HotKeyControl(string Name)
        {
            this.grid = new Grid();
            this.label = new Label();
            this.label.Content = Name;
            this.comboBox = new ComboBox();
            this.comboBox.Items.Add("none");
            this.comboBox.Items.Add("Ctrl");
            this.comboBox.Items.Add("Shift");
            this.textBox = new TextBox();
        }

        public Grid CreateHotKeyControl()
        {
            this.grid.Width = 300;
            this.grid.HorizontalAlignment = HorizontalAlignment.Left;
            ColumnDefinition col0 = new ColumnDefinition();
            ColumnDefinition col1 = new ColumnDefinition();
            ColumnDefinition col2 = new ColumnDefinition();
            this.grid.ColumnDefinitions.Add(col0);
            this.grid.ColumnDefinitions.Add(col1);
            this.grid.ColumnDefinitions.Add(col2);
            RowDefinition row0 = new RowDefinition();
            this.grid.RowDefinitions.Add(row0);
            this.label.Width = 60;
            this.label.HorizontalAlignment = HorizontalAlignment.Left;
            this.label.Margin = new Thickness(10);
            Grid.SetColumn(this.label, 0);
            Grid.SetRow(this.label, 0);
            this.comboBox.Width = 60;
            this.comboBox.HorizontalAlignment = HorizontalAlignment.Left;
            this.comboBox.Margin = new Thickness(10);
            Grid.SetColumn(this.comboBox, 1);
            Grid.SetRow(this.comboBox, 0);
            this.textBox.Width = 60;
            this.textBox.HorizontalAlignment = HorizontalAlignment.Left;
            this.textBox.Margin = new Thickness(10);
            Grid.SetColumn(this.textBox, 2);
            Grid.SetRow(this.textBox, 0);
            this.grid.Children.Add(this.label);
            this.grid.Children.Add(this.comboBox);
            this.grid.Children.Add(this.textBox);
            return this.grid;
        }

        public string GetHotKeyModifer()
        {
            return this.comboBox.Text;
        }
        public void SetHotKeyModifer(string Modifer)
        {
            this.comboBox.Text = Modifer;
        }

        public string GetHotKey()
        {
            return this.textBox.Text.Trim().ToUpper();
        }
        public void SetHotKey(string HotKey)
        {
            this.textBox.Text = HotKey;
        }
    }
}
