using System;
using System.Collections.Generic;
using System.Data;
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
    /// Interaction logic for SearchPageView.xaml
    /// </summary>
    public partial class SearchPageView : Page
    {
        private ScrollViewer scrollViewer = new ScrollViewer();

        private DockPanel dockPanel = new DockPanel();
        private Button homeButton = new Button();

        private StackPanel searchStackPanel = new StackPanel();
        private GroupBox searchByGroupBox = new GroupBox();
        public GroupBox SearchByGroupBox
        {
            get { return this.searchByGroupBox; }
        }
        private StackPanel searchByStackPanel = new StackPanel();
        private RadioButton communityRadio = new RadioButton();
        public RadioButton CommunityRadio
        {
            get { return this.communityRadio; }
        }
        private RadioButton blockRadio = new RadioButton();
        public RadioButton BlockRadio
        {
            get { return this.blockRadio; }
        }
        private RadioButton byStatRadio = new RadioButton();
        public RadioButton ByStatRadio
        {
            get { return this.byStatRadio; }
        }

        private ComboBox searchSelectionComboBox = new ComboBox();
        public ComboBox SearchSelectionComboBox
        {
            get { return this.searchSelectionComboBox; }
        }

        private GroupBox refineSeachGroupBox = new GroupBox();
        public GroupBox RefineSeachGroupBox
        {
            get { return this.refineSeachGroupBox; }
        }
        private ComboBox refineSearchComboBox = new ComboBox();
        public ComboBox RefineSeachComboBox
        {
            get { return this.refineSearchComboBox; }
        }

        // Expander
        private Expander advancedExpander = new Expander();
        public Expander AdvancedExpander
        {
            get { return this.advancedExpander; }
        }
        private Grid expanderGrid = new Grid();
        private Label showTopLabel = new Label();
        public Label ShowTopLabel
        {
            get { return this.showTopLabel; }
        }
        private TextBox showTopTextBox = new TextBox();
        public TextBox ShowTopTextBox
        {
            get { return this.showTopTextBox; }
        }
        private RadioButton ascending = new RadioButton();
        public RadioButton Ascending
        {
            get { return this.ascending; }
        }
        private RadioButton descending = new RadioButton();
        public RadioButton Descending
        {
            get { return this.descending; }
        }
        // Expander

        private Button searchButton = new Button();

        private GroupBox currentSearchGroupBox = new GroupBox();
        public GroupBox CurrentSearchGroupBox
        {
            get { return this.currentSearchGroupBox; }
        }
        private StackPanel currentSeachStackPanel = new StackPanel();
        private Button saveCurrentButton = new Button();
        public Button SaveCurrentButton
        {
            get { return this.saveCurrentButton; }
        }
        private ComboBox loadCurrentComboBox = new ComboBox();
        public ComboBox LoadCurrentComboBox
        {
            get { return this.loadCurrentComboBox; }
        }
        private Button loadCurrentButton = new Button();
        public Button LoadCurrentButton
        {
            get { return this.loadCurrentButton; }
        }

        private GroupBox exportSearchGroupBox = new GroupBox();
        public GroupBox ExportSearchGroupBox
        {
            get { return this.exportSearchGroupBox; }
        }
        private StackPanel exportStackPanel = new StackPanel();
        private Button exportSeachButton = new Button();
        public Button ExportSeachButton
        {
            get { return this.exportSeachButton; }
        }
        private Button importSearchButton = new Button();
        public Button ImportSearchButton
        {
            get { return this.importSearchButton; }
        }

        private DockPanel resultsDockPanel = new DockPanel();
        private Label resultsLabel = new Label();
        public Label ResultsLabel
        {
            get { return this.resultsLabel; }
        }
        private StackPanel resultsInfoStackPanel = new StackPanel();
        private ListBox resultsListBox = new ListBox();

        public SearchPageView()
        {
            InitializeComponent();
            
            this.homeButton.Content = Utilities.ImageTools.SetButtonImage(@"/Assets/home.png", 50, 50, 50);
            this.homeButton.Click += HomeButtonClick;
            this.homeButton.Margin = new Thickness(10);

            DockPanel.SetDock(this.homeButton, Dock.Top);

            this.searchByGroupBox.Margin = new Thickness(10);
            this.searchByGroupBox.Width = 300;
            this.communityRadio.Checked += communityRadio_Checked;
            this.communityRadio.Margin = new Thickness(10);
            this.communityRadio.IsChecked = true;
            this.blockRadio.Checked += blockRadio_Checked;
            this.blockRadio.Margin = new Thickness(10);
            this.byStatRadio.Checked += byStatRadio_Checked;
            this.byStatRadio.Margin = new Thickness(10);

            this.searchByStackPanel.Children.Add(this.communityRadio);
            this.searchByStackPanel.Children.Add(this.blockRadio);
            this.searchByStackPanel.Children.Add(this.byStatRadio);
            this.searchByGroupBox.Content = searchByStackPanel;

            this.searchSelectionComboBox.Width = 300;
            this.searchSelectionComboBox.Margin = new Thickness(10);

            this.refineSeachGroupBox.Margin = new Thickness(10);
            this.refineSeachGroupBox.Width = 300;
            this.refineSearchComboBox.Margin = new Thickness(10);
            this.refineSearchComboBox.Items.Add("Crime Rate");
            this.refineSearchComboBox.Items.Add("Per Capita Income");
            this.refineSearchComboBox.Items.Add("Hardship Index");
            this.refineSearchComboBox.SelectedIndex = 0;
            this.refineSeachGroupBox.Content = this.refineSearchComboBox;

            // Expander
            this.advancedExpander.Margin = new Thickness(10);
            ColumnDefinition aexCol0 = new ColumnDefinition();
            ColumnDefinition aexCol1 = new ColumnDefinition();
            this.expanderGrid.ColumnDefinitions.Add(aexCol0);
            this.expanderGrid.ColumnDefinitions.Add(aexCol1);
            RowDefinition aexRow0 = new RowDefinition();
            RowDefinition aexRow1 = new RowDefinition();
            RowDefinition aexRow2 = new RowDefinition();
            this.expanderGrid.RowDefinitions.Add(aexRow0);
            this.expanderGrid.RowDefinitions.Add(aexRow1);
            this.expanderGrid.RowDefinitions.Add(aexRow2);

            Grid.SetColumn(this.showTopLabel, 0);
            Grid.SetRow(this.showTopLabel, 0);
            Grid.SetColumn(this.showTopTextBox, 1);
            Grid.SetRow(this.showTopTextBox, 0);

            this.ascending.Content = "Ascending (best to worst)";
            Grid.SetColumn(this.ascending, 0);
            Grid.SetRow(this.ascending, 1);
            this.descending.Content = "Descending (worst to best)";
            this.descending.IsChecked = true;
            Grid.SetColumn(this.descending, 0);
            Grid.SetRow(this.descending, 2);

            this.expanderGrid.Children.Add(this.showTopLabel);
            this.expanderGrid.Children.Add(this.showTopTextBox);
            this.expanderGrid.Children.Add(this.ascending);
            this.expanderGrid.Children.Add(this.descending);
            this.advancedExpander.Content = this.expanderGrid;
            // Expander

            this.searchButton.Content = Utilities.ImageTools.SetButtonImage(@"/Assets/search.png", 40, 40, 40);
            this.searchButton.Margin = new Thickness(10);
            this.searchButton.Click += searchButton_Click;

            this.currentSearchGroupBox.Margin = new Thickness(10);

            this.saveCurrentButton.Margin = new Thickness(10);
            this.saveCurrentButton.Height = 24;
            this.saveCurrentButton.Click += saveCurrentButton_Click;

            this.loadCurrentComboBox.Margin = new Thickness(10);

            this.LoadCurrentButton.Margin = new Thickness(10);
            this.LoadCurrentButton.Height = 24;
            this.LoadCurrentButton.Click += LoadCurrentButton_Click;

            this.currentSeachStackPanel.Children.Add(this.saveCurrentButton);
            this.currentSeachStackPanel.Children.Add(this.loadCurrentComboBox);
            this.currentSeachStackPanel.Children.Add(this.LoadCurrentButton);
            this.currentSearchGroupBox.Content = this.currentSeachStackPanel;

            this.exportSearchGroupBox.Margin = new Thickness(10);

            this.exportSeachButton.Margin = new Thickness(10);
            this.exportSeachButton.Height = 24;
            this.exportSeachButton.Click += exportSeachButton_Click;

            this.importSearchButton.Margin = new Thickness(10);
            this.importSearchButton.Height = 24;
            this.importSearchButton.Click += importSearchButton_Click;

            this.exportStackPanel.Children.Add(this.exportSeachButton);
            this.exportStackPanel.Children.Add(this.importSearchButton);
            this.exportSearchGroupBox.Content = this.exportStackPanel;

            this.searchStackPanel.Children.Add(this.searchByGroupBox);
            this.searchStackPanel.Children.Add(this.searchSelectionComboBox);
            this.searchStackPanel.Children.Add(this.refineSeachGroupBox);
            this.searchStackPanel.Children.Add(this.advancedExpander);
            this.searchStackPanel.Children.Add(this.searchButton);
            this.searchStackPanel.Children.Add(this.currentSearchGroupBox);
            this.searchStackPanel.Children.Add(this.exportSearchGroupBox);

            DockPanel.SetDock(this.searchStackPanel, Dock.Left);

            this.resultsDockPanel.LastChildFill = true;

            this.resultsLabel.Margin = new Thickness(10);

            DockPanel.SetDock(this.resultsLabel, Dock.Top);

            this.resultsInfoStackPanel.Margin = new Thickness(10);

            DockPanel.SetDock(this.resultsInfoStackPanel, Dock.Top);

            this.resultsListBox.Margin = new Thickness(10);

            DockPanel.SetDock(this.resultsListBox, Dock.Bottom);

            this.resultsDockPanel.Children.Add(this.resultsLabel);
            this.resultsDockPanel.Children.Add(this.resultsInfoStackPanel);

            this.resultsDockPanel.Children.Add(this.resultsListBox);

            DockPanel.SetDock(this.resultsDockPanel, Dock.Right);

            this.dockPanel.Children.Add(this.homeButton);
            this.dockPanel.Children.Add(this.searchStackPanel);
            this.dockPanel.Children.Add(this.resultsDockPanel);

            this.scrollViewer.VerticalScrollBarVisibility = ScrollBarVisibility.Visible;
            this.scrollViewer.HorizontalScrollBarVisibility = ScrollBarVisibility.Hidden;
            this.scrollViewer.Content = this.dockPanel;
            this.Content = this.scrollViewer;
        }

        private void HomeButtonClick(object sender, RoutedEventArgs e)
        {
            NIKernel.Instance.LoadPageView(Constants.PageViewID.HomePageView);
        }

        void communityRadio_Checked(object sender, RoutedEventArgs e)
        {
            this.advancedExpander.IsEnabled = false;
            this.searchSelectionComboBox.IsEnabled = true;
            this.refineSearchComboBox.IsEnabled = false;
            EnumerableRowCollection<Database.CommunityArea> commAreas = NIKernel.Instance.DBInstance.GetCommunityAreasFromDataTable(Constants.DataTables.CensusDataTable);
            this.searchSelectionComboBox.Items.Clear();
            this.searchSelectionComboBox.BeginInit();
            foreach (Database.CommunityArea ca in commAreas)
            {
                this.searchSelectionComboBox.Items.Add(ca);
            }
            this.searchSelectionComboBox.EndInit();
            this.searchSelectionComboBox.SelectedIndex = 0;
        }

        void blockRadio_Checked(object sender, RoutedEventArgs e)
        {
            this.advancedExpander.IsEnabled = false;
            this.searchSelectionComboBox.IsEnabled = true;
            this.refineSearchComboBox.IsEnabled = false;
            IEnumerable<String> blockNames = NIKernel.Instance.DBInstance.GetBlocksFromDataTable(Constants.DataTables.CrimesDataTable);
            this.searchSelectionComboBox.Items.Clear();
            this.searchSelectionComboBox.BeginInit();
            foreach (String bn in blockNames)
            {
                this.searchSelectionComboBox.Items.Add(bn);
            }
            this.searchSelectionComboBox.EndInit();
            this.searchSelectionComboBox.SelectedIndex = 0;
        }

        void byStatRadio_Checked(object sender, RoutedEventArgs e)
        {
            this.advancedExpander.IsEnabled = true;
            this.searchSelectionComboBox.IsEnabled = false;
            this.refineSearchComboBox.IsEnabled = true;
        }

        void searchButton_Click(object sender, RoutedEventArgs e)
        {
            PerformSearchAction();
        }

        void saveCurrentButton_Click(object sender, RoutedEventArgs e)
        {
            if (this.resultsListBox.Items.Count < 1)
            {
                MessageBox.Show("No search data to save.", "Save Current", MessageBoxButton.OK, MessageBoxImage.Information);
                return;
            }
            if (this.communityRadio.IsChecked == true)
            {
                CurrentSearch.ByCommunitySearch bcs = new CurrentSearch.ByCommunitySearch();
                bcs.CommArea = (Database.CommunityArea)this.searchSelectionComboBox.SelectedItem;
                this.loadCurrentComboBox.Items.Add(bcs.CommArea);
                if (this.loadCurrentComboBox.Items.Count > 0)
                {
                    this.loadCurrentComboBox.SelectedItem = bcs.CommArea;
                }
            }
            else if (this.blockRadio.IsChecked == true)
            {
                CurrentSearch.ByBlockSearch bbs = new CurrentSearch.ByBlockSearch();
                bbs.BlockName = this.searchSelectionComboBox.SelectedItem.ToString();
                this.loadCurrentComboBox.Items.Add(bbs);
                if (this.loadCurrentComboBox.Items.Count > 0)
                {
                    this.loadCurrentComboBox.SelectedItem = bbs;
                }
            }
            else
            {
                MessageBox.Show("The save current option is only available for community and block searches.", "Save Current", MessageBoxButton.OK, MessageBoxImage.Information);
            }
        }

        void LoadCurrentButton_Click(object sender, RoutedEventArgs e)
        {
            if (this.loadCurrentComboBox.Items.Count < 1)
            {
                MessageBox.Show("No search data to load.", "Load Current", MessageBoxButton.OK, MessageBoxImage.Information);
                return;
            }
            if (this.loadCurrentComboBox.SelectedItem is Database.CommunityArea)
            {
                Database.CommunityArea ca = (Database.CommunityArea)this.loadCurrentComboBox.SelectedItem;
                this.communityRadio.IsChecked = true;
                this.searchSelectionComboBox.SelectedItem = ca;
                PerformSearchActionForCommArea(ca);
            }
            if (this.loadCurrentComboBox.SelectedItem is CurrentSearch.ByBlockSearch)
            {
                CurrentSearch.ByBlockSearch tt = (CurrentSearch.ByBlockSearch)this.loadCurrentComboBox.SelectedItem;
                this.blockRadio.IsChecked = true;
                this.searchSelectionComboBox.SelectedItem = tt;
                PerformSearchActionForBlock(tt.BlockName);
            }
        }

        void exportSeachButton_Click(object sender, RoutedEventArgs e)
        {
            if (this.communityRadio.IsChecked == true)
            {
                if (this.resultsListBox.Items.Count > 0)
                {
                    Utilities.ExportTools.comboIndex = this.searchSelectionComboBox.SelectedIndex.ToString();
                    Utilities.ExportTools.ExportData();
                    MessageBox.Show("Search data saved!", "Export", MessageBoxButton.OK);
                }
                else
                {
                    MessageBox.Show("No search to save!", "Export", MessageBoxButton.OK, MessageBoxImage.Exclamation);
                }
            }
            else
            {
                MessageBox.Show("The export feature is only available for community searches.", "Export", MessageBoxButton.OK, MessageBoxImage.Information);
            }
        }

        void importSearchButton_Click(object sender, RoutedEventArgs e)
        {
            int index = Utilities.ImportTools.ImportSeachData();
            this.searchSelectionComboBox.SelectedIndex = index;
            Database.CommunityArea ca = (Database.CommunityArea)this.searchSelectionComboBox.SelectedItem;
            this.communityRadio.IsChecked = true;
            PerformSearchActionForCommArea(ca);
            //
            CurrentSearch.ByCommunitySearch bcs = new CurrentSearch.ByCommunitySearch();
            bcs.CommArea = (Database.CommunityArea)this.searchSelectionComboBox.SelectedItem;
            this.loadCurrentComboBox.Items.Add(bcs.CommArea);
            if (this.loadCurrentComboBox.Items.Count > 0)
            {
                this.loadCurrentComboBox.SelectedItem = bcs.CommArea;
            }
        }

        private void PerformSearchAction()
        {
            // Do these actions when searching by community...
            if (this.communityRadio.IsChecked == true)
            {
                IEnumerable<Database.CrimeType> crimes =
                    NIKernel.Instance.DBInstance.GetCommunityCrimeDataFromDataTable(Constants.DataTables.CrimesDataTable, ((Database.CommunityArea)this.searchSelectionComboBox.SelectedItem).CommunityID);
                IEnumerable<int?> perCapitaIncome =
                    NIKernel.Instance.DBInstance.GetPerCapitaIncome(Constants.DataTables.CensusDataTable, ((Database.CommunityArea)this.searchSelectionComboBox.SelectedItem).CommunityID);
                IEnumerable<int?> hardshipIndex =
                    NIKernel.Instance.DBInstance.GetHardshipIndex(Constants.DataTables.CensusDataTable, ((Database.CommunityArea)this.searchSelectionComboBox.SelectedItem).CommunityID);

                Views.Controls.SearchDataResult sdr = new Controls.SearchDataResult(
                    ((Database.CommunityArea)this.searchSelectionComboBox.SelectedItem).CommunityName, crimes, perCapitaIncome, hardshipIndex);

                this.resultsListBox.Items.Clear();
                this.resultsListBox.BeginInit();
                this.resultsListBox.Items.Add(sdr.GetDataControl());
                this.resultsListBox.EndInit();
            }
            // Do these actions when searching by block...
            if (this.blockRadio.IsChecked == true)
            {
                IEnumerable<decimal?> tif = 
                    NIKernel.Instance.DBInstance.GetTIFBalance(Constants.DataTables.TIFDataTable, this.searchSelectionComboBox.Text);

                Views.Controls.ByBlockSearchDataResult dr = new Controls.ByBlockSearchDataResult(
                    (string)this.searchSelectionComboBox.SelectedItem, tif.First());

                this.resultsListBox.Items.Clear();
                this.resultsListBox.BeginInit();
                this.resultsListBox.Items.Add(dr.GetDataControl());
                this.resultsListBox.EndInit();
            }
            // Do these actions when searching by statistic
            if (this.byStatRadio.IsChecked == true)
            {
                // Get a list of all the community names.
                EnumerableRowCollection<Database.CommunityArea> commAreasList = NIKernel.Instance.DBInstance.GetCommunityAreasFromDataTable(Constants.DataTables.CensusDataTable);
                // For each community area in the list, we need to get it's crime percentage, save all results in a list
                Dictionary<string, float> values = new Dictionary<string, float>();
                Dictionary<string, int?> valuesPCI = new Dictionary<string, int?>();
                foreach (Database.CommunityArea ca in commAreasList)
                {
                    if (this.refineSearchComboBox.Text == "Crime Rate")
                    {
                        float p = NIKernel.Instance.DBInstance.GetCommunityCrimeDataPercentage(Constants.DataTables.CrimesDataTable, ca.CommunityID);
                        values.Add(ca.CommunityName, p);
                    }
                    else if (this.refineSearchComboBox.Text == "Per Capita Income")
                    {
                        if (ca.CommunityID == 0) { continue; }
                        IEnumerable<int?> p = NIKernel.Instance.DBInstance.GetPerCapitaIncome(Constants.DataTables.CensusDataTable, ca.CommunityID);
                        valuesPCI.Add(ca.CommunityName, p.First());
                    }
                    else if (this.refineSearchComboBox.Text == "Hardship Index")
                    {
                        if (ca.CommunityID == 0) { continue; }
                        IEnumerable<int?> p = NIKernel.Instance.DBInstance.GetHardshipIndex(Constants.DataTables.CensusDataTable, ca.CommunityID);
                        valuesPCI.Add(ca.CommunityName, p.First());
                    }
                }
                // Now traverse the list of data and display the controls in the results list box
                if (this.refineSearchComboBox.Text == "Crime Rate")
                {
                    var sortedValuesAsc = from entry in values orderby entry.Value ascending select entry;
                    var sortedValuesDes = from entry in values orderby entry.Value descending select entry;
                    // Now we need to determine how many to display
                    int howMany = Convert.ToInt32(this.showTopTextBox.Text.Trim());
                    int index = 0;
                    this.resultsListBox.Items.Clear();
                    this.resultsListBox.BeginInit();
                    if (this.ascending.IsChecked == true)
                    {
                        foreach (KeyValuePair<string, float> kvp in sortedValuesAsc)
                        {
                            Console.WriteLine(kvp.Key + ": " + kvp.Value.ToString() + "%");

                            Views.Controls.StatSearchResult ssr = new Controls.StatSearchResult(kvp.Key, "Crime Rate", kvp.Value.ToString() + "% of all crimes in Chicago");
                            this.resultsListBox.Items.Add(ssr.GetDataControl());

                            if (index >= howMany)
                            {
                                break;
                            }
                            index++;
                        }
                    }
                    else
                    {
                        foreach (KeyValuePair<string, float> kvp in sortedValuesDes)
                        {
                            Console.WriteLine(kvp.Key + ": " + kvp.Value.ToString() + "%");

                            Views.Controls.StatSearchResult ssr = new Controls.StatSearchResult(kvp.Key, "Crime Rate", kvp.Value.ToString() + "% of all crimes in Chicago");
                            this.resultsListBox.Items.Add(ssr.GetDataControl());

                            if (index >= howMany)
                            {
                                break;
                            }
                            index++;
                        }
                    }
                    this.resultsListBox.EndInit();
                }
                else if (this.refineSearchComboBox.Text == "Per Capita Income")
                {
                    var sortedValuesAsc = from entry in valuesPCI orderby entry.Value ascending select entry;
                    var sortedValuesDes = from entry in valuesPCI orderby entry.Value descending select entry;
                    // Now we need to determine how many to display
                    int howMany = Convert.ToInt32(this.showTopTextBox.Text.Trim());
                    int index = 0;
                    this.resultsListBox.Items.Clear();
                    this.resultsListBox.BeginInit();
                    if (this.ascending.IsChecked == true)
                    {
                        foreach (KeyValuePair<string, int?> kvp in sortedValuesDes)
                        {
                            Console.WriteLine(kvp.Key + ": $" + kvp.Value.ToString() + ".00");

                            Views.Controls.StatSearchResult ssr = new Controls.StatSearchResult(kvp.Key, "Per Capita Income", kvp.Value.ToString() + ".00");
                            this.resultsListBox.Items.Add(ssr.GetDataControl());

                            if (index >= howMany)
                            {
                                break;
                            }
                            index++;
                        }
                    }
                    else
                    {
                        foreach (KeyValuePair<string, int?> kvp in sortedValuesAsc)
                        {
                            Console.WriteLine(kvp.Key + ": $" + kvp.Value.ToString() + ".00");

                            Views.Controls.StatSearchResult ssr = new Controls.StatSearchResult(kvp.Key, "Per Capita Income", kvp.Value.ToString() + ".00");
                            this.resultsListBox.Items.Add(ssr.GetDataControl());

                            if (index >= howMany)
                            {
                                break;
                            }
                            index++;
                        }
                    }
                    this.resultsListBox.EndInit();
                }
                else if (this.refineSearchComboBox.Text == "Hardship Index")
                {
                    var sortedValuesAsc = from entry in valuesPCI orderby entry.Value ascending select entry;
                    var sortedValuesDes = from entry in valuesPCI orderby entry.Value descending select entry;
                    // Now we need to determine how many to display
                    int howMany = Convert.ToInt32(this.showTopTextBox.Text.Trim());
                    int index = 0;
                    this.resultsListBox.Items.Clear();
                    this.resultsListBox.BeginInit();
                    if (this.ascending.IsChecked == true)
                    {
                        foreach (KeyValuePair<string, int?> kvp in sortedValuesAsc)
                        {
                            Console.WriteLine(kvp.Key + ": " + kvp.Value.ToString());

                            Views.Controls.StatSearchResult ssr = new Controls.StatSearchResult(kvp.Key, "Hardship Index", kvp.Value.ToString() + " out of 100");
                            this.resultsListBox.Items.Add(ssr.GetDataControl());

                            if (index >= howMany)
                            {
                                break;
                            }
                            index++;
                        }
                    }
                    else
                    {
                        foreach (KeyValuePair<string, int?> kvp in sortedValuesDes)
                        {
                            Console.WriteLine(kvp.Key + ": " + kvp.Value.ToString());

                            Views.Controls.StatSearchResult ssr = new Controls.StatSearchResult(kvp.Key, "Hardship Index", kvp.Value.ToString() + " out of 100");
                            this.resultsListBox.Items.Add(ssr.GetDataControl());

                            if (index >= howMany)
                            {
                                break;
                            }
                            index++;
                        }
                    }
                    this.resultsListBox.EndInit();
                }
                
            }
        }

        // Method for use with load current when loading a community area search
        private void PerformSearchActionForCommArea(Database.CommunityArea CommArea)
        {
            IEnumerable<Database.CrimeType> crimes =
                    NIKernel.Instance.DBInstance.GetCommunityCrimeDataFromDataTable(Constants.DataTables.CrimesDataTable, CommArea.CommunityID);
            IEnumerable<int?> perCapitaIncome =
                NIKernel.Instance.DBInstance.GetPerCapitaIncome(Constants.DataTables.CensusDataTable, CommArea.CommunityID);
            IEnumerable<int?> hardshipIndex =
                NIKernel.Instance.DBInstance.GetHardshipIndex(Constants.DataTables.CensusDataTable, CommArea.CommunityID);

            Views.Controls.SearchDataResult sdr = new Controls.SearchDataResult(CommArea.CommunityName, crimes, perCapitaIncome, hardshipIndex);

            this.resultsListBox.Items.Clear();
            this.resultsListBox.BeginInit();
            this.resultsListBox.Items.Add(sdr.GetDataControl());
            this.resultsListBox.EndInit();
        }

        // Method for use with load current when loading by block search
        private void PerformSearchActionForBlock(string BlockName)
        {
            IEnumerable<decimal?> tif =
                    NIKernel.Instance.DBInstance.GetTIFBalance(Constants.DataTables.TIFDataTable, BlockName);

            Views.Controls.ByBlockSearchDataResult dr = new Controls.ByBlockSearchDataResult(
                BlockName, tif.First());

            this.resultsListBox.Items.Clear();
            this.resultsListBox.BeginInit();
            this.resultsListBox.Items.Add(dr.GetDataControl());
            this.resultsListBox.EndInit();
        }
    }
}
