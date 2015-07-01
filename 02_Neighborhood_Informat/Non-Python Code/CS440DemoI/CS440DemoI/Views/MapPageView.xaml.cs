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
    /// Interaction logic for MapPageView.xaml
    /// </summary>
    public partial class MapPageView : Page
    {
        private DockPanel dockPanel = new DockPanel();
        private Button homeButton = new Button();
        private StackPanel stackPanel = new StackPanel();
        private Label mapLabel = new Label();
        public Label MapLabel
        {
            get { return this.mapLabel; }
        }
        private ScrollViewer scrollViewer = new ScrollViewer();
        private Image mapImage = new Image();

        public MapPageView()
        {
            InitializeComponent();

            this.dockPanel.LastChildFill = true;

            this.homeButton.Content = Utilities.ImageTools.SetButtonImage(@"/Assets/home.png", 50, 50, 50);
            this.homeButton.Click += HomeButtonClick;
            this.homeButton.Margin = new Thickness(10);

            DockPanel.SetDock(this.homeButton, Dock.Top);

            this.mapLabel.FontSize = 24.0;

            BitmapImage neighborhoodImage = new BitmapImage();
            neighborhoodImage.BeginInit();
            neighborhoodImage.UriSource = new Uri(@"/Assets/neighborhoods.jpg", UriKind.RelativeOrAbsolute);
            neighborhoodImage.EndInit();
            this.mapImage.Source = neighborhoodImage;

            // The sizing of this image could probably be better, but if we present in full-screen mode, it should be ok.

            this.stackPanel.Margin = new Thickness(10);
            this.stackPanel.Children.Add(this.mapLabel);
            this.stackPanel.Children.Add(this.mapImage);

            DockPanel.SetDock(this.stackPanel, Dock.Bottom);

            this.dockPanel.Children.Add(this.homeButton);
            this.dockPanel.Children.Add(this.stackPanel);

            this.scrollViewer.Content = this.dockPanel;

            this.Content = this.scrollViewer;
        }

        void HomeButtonClick(object sender, RoutedEventArgs e)
        {
            NIKernel.Instance.LoadPageView(Constants.PageViewID.HomePageView);
        }
    }
}
