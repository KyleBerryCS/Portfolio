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
    /// Interaction logic for SettingsPageView.xaml
    /// </summary>
    public partial class SettingsPageView : Page
    {
        private ScrollViewer scrollViewer = new ScrollViewer();
        private DockPanel dockPanel = new DockPanel();
        private Button homeButton = new Button();
        private StackPanel stackPanel = new StackPanel();
        private Label settingsLabel = new Label();
        public Label SettingsLabel
        {
            get { return this.settingsLabel; }
        }
        private GroupBox languageGroupBox = new GroupBox();
        public GroupBox LanguageGroupBox
        {
            get { return this.languageGroupBox; }
        }
        private Grid languageGrid = new Grid();
        private RadioButton englishRad = new RadioButton();
        public RadioButton EnglishRad
        {
            get { return this.englishRad; }
        }
        private RadioButton spanishRad = new RadioButton();
        public RadioButton SpanishRad
        {
            get { return this.spanishRad; }
        }
        private GroupBox hotkeyGroupBox = new GroupBox();
        public GroupBox HotKeyGroupBox
        {
            get { return this.hotkeyGroupBox; }
        }
        private StackPanel hotKeyStackPanel = new StackPanel();
        private Views.Controls.HotKeyControl hkeSearch = new Views.Controls.HotKeyControl("Search");
        public Label HKESearchLabel
        {
            get { return this.hkeSearch.HKLabel; }
        }
        private Views.Controls.HotKeyControl hkeHome = new Views.Controls.HotKeyControl("Home");
        public Label HKEHomeLabel
        {
            get { return this.hkeHome.HKLabel; }
        }
        private Views.Controls.HotKeyControl hkeMap = new Views.Controls.HotKeyControl("Map");
        public Label HKEMapLabel
        {
            get { return this.hkeMap.HKLabel; }
        }
        private Views.Controls.HotKeyControl hkeHelp = new Views.Controls.HotKeyControl("Help");
        public Label HKEHelpLabel
        {
            get { return this.hkeHelp.HKLabel; }
        }
        private Views.Controls.HotKeyControl hkeSettings = new Views.Controls.HotKeyControl("Settings");
        public Label HKESettingsLabel
        {
            get { return this.hkeSettings.HKLabel; }
        }
        private Button applyButton = new Button();
        public Button ApplyButton
        {
            get { return this.applyButton; }
        }

        public SettingsPageView()
        {
            InitializeComponent();

            this.dockPanel.LastChildFill = true;

            this.homeButton.Content = Utilities.ImageTools.SetButtonImage(@"/Assets/home.png", 50, 50, 50);
            this.homeButton.Click += HomeButtonClick;
            this.homeButton.Margin = new Thickness(10);

            DockPanel.SetDock(this.homeButton, Dock.Top);

            this.settingsLabel.FontSize = 24.0;
            this.settingsLabel.Margin = new Thickness(10);

            ColumnDefinition langCol0 = new ColumnDefinition();
            ColumnDefinition langCol1 = new ColumnDefinition();
            this.languageGrid.ColumnDefinitions.Add(langCol0);
            this.languageGrid.ColumnDefinitions.Add(langCol1);
            RowDefinition langRow0 = new RowDefinition();
            this.languageGrid.RowDefinitions.Add(langRow0);

            this.englishRad.Margin = new Thickness(10);
            this.englishRad.Checked += englishRad_Checked;
            Grid.SetColumn(this.englishRad, 0);
            Grid.SetRow(this.englishRad, 0);
            this.spanishRad.Margin = new Thickness(10);
            this.spanishRad.Checked += spanishRad_Checked;
            Grid.SetColumn(this.spanishRad, 1);
            Grid.SetRow(this.spanishRad, 0);

            if (Properties.Settings.Default.IsInEnglish == true)
            {
                this.englishRad.IsChecked = true;
            }
            else
            {
                this.spanishRad.IsChecked = true;
            }

            this.languageGrid.Children.Add(this.englishRad);
            this.languageGrid.Children.Add(this.spanishRad);

            this.languageGroupBox.Content = this.languageGrid;
            this.languageGroupBox.Margin = new Thickness(10);

            this.hotkeyGroupBox.Margin = new Thickness(10);
            this.hkeHome.SetHotKeyModifer(Properties.Settings.Default.HomeHKM);
            this.hkeHome.SetHotKey(Properties.Settings.Default.HomeHK);
            this.hotKeyStackPanel.Children.Add(hkeHome.CreateHotKeyControl());

            this.hkeSearch.SetHotKeyModifer(Properties.Settings.Default.SearchHKM);
            this.hkeSearch.SetHotKey(Properties.Settings.Default.SearchHK);
            this.hotKeyStackPanel.Children.Add(hkeSearch.CreateHotKeyControl());

            this.hkeMap.SetHotKeyModifer(Properties.Settings.Default.MapHKM);
            this.hkeMap.SetHotKey(Properties.Settings.Default.MapHK);
            this.hotKeyStackPanel.Children.Add(hkeMap.CreateHotKeyControl());

            this.hkeSettings.SetHotKeyModifer(Properties.Settings.Default.SettingsHKM);
            this.hkeSettings.SetHotKey(Properties.Settings.Default.SettingsHK);
            this.hotKeyStackPanel.Children.Add(hkeSettings.CreateHotKeyControl());

            this.hkeHelp.SetHotKeyModifer(Properties.Settings.Default.HelpHKM);
            this.hkeHelp.SetHotKey(Properties.Settings.Default.HelpHK);
            this.hotKeyStackPanel.Children.Add(hkeHelp.CreateHotKeyControl());

            this.hotkeyGroupBox.Content = this.hotKeyStackPanel;

            this.applyButton.Click += applyButton_Click;
            this.applyButton.Width = 120;
            this.applyButton.Height = 24;
            this.applyButton.Margin = new Thickness(10);
            this.applyButton.HorizontalAlignment = System.Windows.HorizontalAlignment.Left;

            this.stackPanel.Children.Add(this.settingsLabel);
            this.stackPanel.Children.Add(this.languageGroupBox);
            this.stackPanel.Children.Add(this.hotkeyGroupBox);
            this.stackPanel.Children.Add(this.applyButton);

            DockPanel.SetDock(this.stackPanel, Dock.Bottom);

            this.dockPanel.Children.Add(this.homeButton);
            this.dockPanel.Children.Add(this.stackPanel);

            this.scrollViewer.Content = this.dockPanel;
            this.scrollViewer.VerticalScrollBarVisibility = ScrollBarVisibility.Visible;
            this.scrollViewer.HorizontalScrollBarVisibility = ScrollBarVisibility.Hidden;

            this.Content = this.scrollViewer;
        }

        void spanishRad_Checked(object sender, RoutedEventArgs e)
        {
            Properties.Settings.Default.IsInEnglish = false;
        }

        void englishRad_Checked(object sender, RoutedEventArgs e)
        {
            Properties.Settings.Default.IsInEnglish = true;
        }

        void HomeButtonClick(object sender, RoutedEventArgs e)
        {
            NIKernel.Instance.LoadPageView(Constants.PageViewID.HomePageView);
        }

        void applyButton_Click(object sender, RoutedEventArgs e)
        {
            Properties.Settings.Default.SearchHKM = this.hkeSearch.GetHotKeyModifer();
            Properties.Settings.Default.SearchHK = this.hkeSearch.GetHotKey();
            Properties.Settings.Default.HomeHKM = this.hkeHome.GetHotKeyModifer();
            Properties.Settings.Default.HomeHK = this.hkeHome.GetHotKey();
            Properties.Settings.Default.MapHKM = this.hkeMap.GetHotKeyModifer();
            Properties.Settings.Default.MapHK = this.hkeMap.GetHotKey();
            Properties.Settings.Default.HelpHKM = this.hkeHelp.GetHotKeyModifer();
            Properties.Settings.Default.HelpHK = this.hkeHelp.GetHotKey();
            Properties.Settings.Default.SettingsHKM = this.hkeSettings.GetHotKeyModifer();
            Properties.Settings.Default.SettingsHK = this.hkeSettings.GetHotKey();
            Properties.Settings.Default.Save();
            Utilities.LanguageTools.UpdateDisplayLanguage();
        }
    }
}
