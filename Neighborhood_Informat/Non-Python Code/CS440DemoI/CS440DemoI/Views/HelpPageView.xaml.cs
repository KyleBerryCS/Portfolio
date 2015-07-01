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
    /// Interaction logic for HelpPageView.xaml
    /// </summary>
    public partial class HelpPageView : Page
    {
        private ScrollViewer scrollViewer = new ScrollViewer();
        private StackPanel helpStackPanel = new StackPanel();
        private Button homeButton = new Button();

        Dictionary<string, string> homeTopics = new Dictionary<string, string>();
        Dictionary<string, string> searchTopics = new Dictionary<string, string>();
        Dictionary<string, string> settingsTopics = new Dictionary<string, string>();
        Dictionary<string, string> mapTopics = new Dictionary<string, string>();

        public HelpPageView()
        {
            InitializeComponent();

            this.homeButton.Content = Utilities.ImageTools.SetButtonImage(@"/Assets/home.png", 50, 50, 50);
            this.homeButton.Click += HomeButtonClick;
            this.homeButton.Margin = new Thickness(10);
            this.helpStackPanel.Children.Add(this.homeButton);

            homeTopics.Add("Search", "Click on the magnifying glass (top left) to enter the search page.");
            homeTopics.Add("Settings", "Click on the gear (bottom left) to enter the settings page.");
            homeTopics.Add("Map", "Click on the map (Top Right) to enter the map page.");
            homeTopics.Add("Help", "Click on the question mark (bottom right) to enter the help page.");
            this.helpStackPanel.Children.Add(CreateHelpTopicControls("Home", homeTopics));

            searchTopics.Add("Search by Community", "To search by a community, first click on the Search page (the magnifying glass on the main screen).  Inside the “search by” box, click the bubble next to “Community”.  Directly below, pull down the drop down and click on the community name that you would like to search.  Finally, click the magnifying glass to complete your search.");
            searchTopics.Add("Search by Block", "To search by a block, first click on the Search page (the magnifying glass on the main screen).  Inside the “search by” box, click the bubble next to “Block”.  Directly below, pull down the drop down and click on the block name that you would like to search.  Finally, click the magnifying glass to complete your search.");
            searchTopics.Add("Refine Search", "To refine the search to search a particular statistic, navigate to the search page (the magnifying glass on the main screen).  Click where you would like to search, the find the “Refine Search By” box.  Inside here, pull down the menu and select the statistics you would like to search.  Finally, click the magnifying glass to complete your search.");
            searchTopics.Add("Advanced Options", "To define the amount of results you wish to see, navigate to the search page (the magnifying glass on the main screen).  On the left hand side, click the down arrow next to “Advanced Options”.  This will open a list of advanced options.  Find the option “Show top:” and enter the amount of results you wish to see in the text box to the right.  This will automatically save and display the amount entered on the next search.");
            searchTopics.Add("Save Current Search", "To the right of the search results there is a “Current Search Options” box.  Click “Save Current Search” to save the search results for the most recent search.");
            searchTopics.Add("Load Current Search", "To load the currently saved search results, to the right of the search results, there is a “Current Search Options” box.  Click “Load Current Search” to load the search results previously saved.");
            searchTopics.Add("Import Search Results", "To import search results, first navigate to the search page (the magnifying glass on the main screen).  At the bottom of the left hand side find the “Export/Import Search Results” box.  Click “Import Results”. This will bring up a file menu where you can navigate to the search results you wish to load.  Highlight the file and click “open” at the bottom of the file menu.");
            searchTopics.Add("Export Search Results", "To export search results, first navigate to the search page (the magnifying glass on the main screen).  Complete the search you wish to export.  At the bottom of the left hand side find the “Export/Import Search Results” box.  Click “Export Results”.  This will bring up a file menu where you can navigate to where you would like to save the results.  Name the file and click “save” at the bottom of the file menu.");
            this.helpStackPanel.Children.Add(CreateHelpTopicControls("Search", searchTopics));

            settingsTopics.Add("Languages", "To switch the language from English to Spanish or Spanish to English, first click on the Settings page (the Gear on the main screen). Under Settings, you will find a “Language” section. Click the checkbox for English to switch to English and Spanish to switch to Spanish. Finally, click “Apply Settings” at the bottom of the settings page to apply the language you selected.");
            settingsTopics.Add("Hot Keys", "Hot keys are quick ways to switch between the settings, home, map, text search, and help pages.  They consist of at most two keys.  The first key is either “control”, “shift”, or none. The second key can be set as any letter on the keyboard.  To set these, first click on the Settings page (the Gear on the main screen). Under Settings, you will find a “Hot Keys” section. You can switch between “control”, “shift, and none by selecting the pull down tab and selecting the setting you would like.  To select the letter you would like you click the text box next to the pull down tab and enter the letter you would like to use.  Finally, click “Apply Settings” at the bottom of the settings page to apply the Hot Keys you selected.");
            this.helpStackPanel.Children.Add(CreateHelpTopicControls("Settings", settingsTopics));

            mapTopics.Add("Using Map Page", "The map page is designed to be a reference for helping you figure out where communities are located.  Click on the map page (the map on the main page).  From here you can look at the map of Chicago and see each community and the name associated with it.");
            this.helpStackPanel.Children.Add(CreateHelpTopicControls("Map", mapTopics));

            this.scrollViewer.VerticalScrollBarVisibility = ScrollBarVisibility.Visible;
            this.scrollViewer.HorizontalScrollBarVisibility = ScrollBarVisibility.Hidden;
            this.scrollViewer.Content = this.helpStackPanel;
            this.Content = this.scrollViewer;
        }

        void HomeButtonClick(object sender, RoutedEventArgs e)
        {
            NIKernel.Instance.LoadPageView(Constants.PageViewID.HomePageView);
        }

        private GroupBox CreateHelpTopicControls(string Name, Dictionary<string, string> HelpTopics)
        {
            GroupBox topicGroupBox = new GroupBox();
            Label topicHeader = new Label();
            topicHeader.FontSize = 20;
            topicHeader.Content = Name;
            StackPanel topicStackPanel = new StackPanel();
            topicGroupBox.Header = topicHeader;
            topicGroupBox.Margin = new Thickness(10);
            foreach (KeyValuePair<string, string> kvp in HelpTopics)
            {
                Label topicTitle = new Label();
                topicTitle.FontSize = 14;
                topicTitle.Content = kvp.Key;
                TextBlock topic = new TextBlock();
                topic.HorizontalAlignment = System.Windows.HorizontalAlignment.Left;
                topic.Margin = new Thickness(20, 10, 10, 10);
                topic.Width = 1000;
                topic.TextWrapping = TextWrapping.Wrap;
                topic.Text = kvp.Value;
                topicStackPanel.Children.Add(topicTitle);
                topicStackPanel.Children.Add(topic);
            }
            topicGroupBox.Content = topicStackPanel;
            return topicGroupBox;
        }
    }
}
