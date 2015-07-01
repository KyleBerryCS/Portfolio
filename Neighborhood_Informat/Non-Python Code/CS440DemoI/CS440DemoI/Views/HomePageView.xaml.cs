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

namespace CS440DemoI.Views
{
    /// <summary>
    /// Interaction logic for HomePageView.xaml
    /// </summary>
    public partial class HomePageView : Page
    {
        private DockPanel dockPanel = new DockPanel();
        private Grid grid = new Grid();
        private Button searchButton = new Button();
        public Button SearchButton
        {
            get { return this.searchButton; }
        }
        private Button mapButton = new Button();
        public Button MapButton
        {
            get { return this.mapButton; }
        }
        private Button settingsButton = new Button();
        public Button SettingsButton
        {
            get { return this.settingsButton; }
        }
        private Button helpButton = new Button();
        public Button HelpButton
        {
            get { return this.helpButton; }
        }

        public HomePageView()
        {
            InitializeComponent();

            this.dockPanel.LastChildFill = true;

            this.searchButton.Content = Utilities.ImageTools.SetButtonImage(@"/Assets/search.png");
            this.searchButton.Click += SearchButtonClick;
            this.searchButton.Margin = new Thickness(10);

            this.mapButton.Content = Utilities.ImageTools.SetButtonImage(@"/Assets/map.png");
            this.mapButton.Click += MapButtonClick;
            this.mapButton.Margin = new Thickness(10);

            this.settingsButton.Content = Utilities.ImageTools.SetButtonImage(@"/Assets/settings.png");
            this.settingsButton.Click += SettingsButtonClick;
            this.settingsButton.Margin = new Thickness(10);

            this.helpButton.Content = Utilities.ImageTools.SetButtonImage(@"/Assets/help.png");
            this.helpButton.Click += HelpButtonClick;
            this.helpButton.Margin = new Thickness(10);

            ColumnDefinition col1 = new ColumnDefinition();
            ColumnDefinition col2 = new ColumnDefinition();
            this.grid.ColumnDefinitions.Add(col1);
            this.grid.ColumnDefinitions.Add(col2);

            RowDefinition row1 = new RowDefinition();
            RowDefinition row2 = new RowDefinition();
            this.grid.RowDefinitions.Add(row1);
            this.grid.RowDefinitions.Add(row2);

            Grid.SetColumn(this.searchButton, 0);
            Grid.SetRow(this.searchButton, 0);
            Grid.SetColumn(this.mapButton, 1);
            Grid.SetRow(this.mapButton, 0);
            Grid.SetColumn(this.settingsButton, 0);
            Grid.SetRow(this.settingsButton, 1);
            Grid.SetColumn(this.helpButton, 1);
            Grid.SetRow(this.helpButton, 1);

            this.grid.Children.Add(this.searchButton);
            this.grid.Children.Add(this.mapButton);
            this.grid.Children.Add(this.settingsButton);
            this.grid.Children.Add(this.helpButton);

            DockPanel.SetDock(this.grid, Dock.Top);

            this.dockPanel.Children.Add(this.grid);

            this.Content = this.dockPanel;
        }

        private void HomeButtonClick(object sender, RoutedEventArgs e)
        {
            NIKernel.Instance.LoadPageView(Constants.PageViewID.HomePageView);
        }

        private void SearchButtonClick(object sender, RoutedEventArgs e)
        {
            NIKernel.Instance.LoadPageView(Constants.PageViewID.SearchPageView);
        }

        private void HelpButtonClick(object sender, RoutedEventArgs e)
        {
            NIKernel.Instance.LoadPageView(Constants.PageViewID.HelpPageView);
        }

        private void SettingsButtonClick(object sender, RoutedEventArgs e)
        {
            NIKernel.Instance.LoadPageView(Constants.PageViewID.SettingsPageView);
        }

        private void MapButtonClick(object sender, RoutedEventArgs e)
        {
            NIKernel.Instance.LoadPageView(Constants.PageViewID.MapViewPage);
        }
    }
}
