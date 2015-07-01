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

namespace CS440DemoI
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            this.WindowState = System.Windows.WindowState.Maximized;
            this.MinHeight = 600;
            this.MinWidth = 800;
            this.KeyDown += MainWindow_KeyDown;

            NIKernel.Instance.InitNIKernel(this);
        }

        void MainWindow_KeyDown(object sender, KeyEventArgs e)
        {
            // Home page hot key setup
            if (Properties.Settings.Default.HomeHKM == "none")
            {
                if (e.Key.ToString().ToUpper() == Properties.Settings.Default.HomeHK)
                {
                    NIKernel.Instance.LoadPageView(Constants.PageViewID.HomePageView);
                }
            }
            if (Properties.Settings.Default.HomeHKM == "Ctrl")
            {
                if ((Keyboard.IsKeyDown(Key.LeftCtrl) || Keyboard.IsKeyDown(Key.RightCtrl)) && e.Key.ToString().ToUpper() == Properties.Settings.Default.HomeHK)
                {
                    NIKernel.Instance.LoadPageView(Constants.PageViewID.HomePageView);
                }
            }
            if (Properties.Settings.Default.HomeHKM == "Shift")
            {
                if ((Keyboard.IsKeyDown(Key.LeftShift) || Keyboard.IsKeyDown(Key.RightShift)) && e.Key.ToString().ToUpper() == Properties.Settings.Default.HomeHK)
                {
                    NIKernel.Instance.LoadPageView(Constants.PageViewID.HomePageView);
                }
            }
            // Search page hot key setup
            if (Properties.Settings.Default.SearchHKM == "none")
            {
                if (e.Key.ToString().ToUpper() == Properties.Settings.Default.SearchHK)
                {
                    NIKernel.Instance.LoadPageView(Constants.PageViewID.SearchPageView);
                }
            }
            if (Properties.Settings.Default.SearchHKM == "Ctrl")
            {
                if ((Keyboard.IsKeyDown(Key.LeftCtrl) || Keyboard.IsKeyDown(Key.RightCtrl)) && e.Key.ToString().ToUpper() == Properties.Settings.Default.SearchHK)
                {
                    NIKernel.Instance.LoadPageView(Constants.PageViewID.SearchPageView);
                }
            }
            if (Properties.Settings.Default.SearchHKM == "Shift")
            {
                if ((Keyboard.IsKeyDown(Key.LeftShift) || Keyboard.IsKeyDown(Key.RightShift)) && e.Key.ToString().ToUpper() == Properties.Settings.Default.SearchHK)
                {
                    NIKernel.Instance.LoadPageView(Constants.PageViewID.SearchPageView);
                }
            }
            // Map page hot key setup
            if (Properties.Settings.Default.MapHKM == "none")
            {
                if (e.Key.ToString().ToUpper() == Properties.Settings.Default.MapHK)
                {
                    NIKernel.Instance.LoadPageView(Constants.PageViewID.MapViewPage);
                }
            }
            if (Properties.Settings.Default.MapHKM == "Ctrl")
            {
                if ((Keyboard.IsKeyDown(Key.LeftCtrl) || Keyboard.IsKeyDown(Key.RightCtrl)) && e.Key.ToString().ToUpper() == Properties.Settings.Default.MapHK)
                {
                    NIKernel.Instance.LoadPageView(Constants.PageViewID.MapViewPage);
                }
            }
            if (Properties.Settings.Default.MapHKM == "Shift")
            {
                if ((Keyboard.IsKeyDown(Key.LeftShift) || Keyboard.IsKeyDown(Key.RightShift)) && e.Key.ToString().ToUpper() == Properties.Settings.Default.MapHK)
                {
                    NIKernel.Instance.LoadPageView(Constants.PageViewID.MapViewPage);
                }
            }
            // Help page hot key setup
            if (Properties.Settings.Default.HelpHKM == "none")
            {
                if (e.Key.ToString().ToUpper() == Properties.Settings.Default.HelpHK)
                {
                    NIKernel.Instance.LoadPageView(Constants.PageViewID.HelpPageView);
                }
            }
            if (Properties.Settings.Default.HelpHKM == "Ctrl")
            {
                if ((Keyboard.IsKeyDown(Key.LeftCtrl) || Keyboard.IsKeyDown(Key.RightCtrl)) && e.Key.ToString().ToUpper() == Properties.Settings.Default.HelpHK)
                {
                    NIKernel.Instance.LoadPageView(Constants.PageViewID.HelpPageView);
                }
            }
            if (Properties.Settings.Default.HelpHKM == "Shift")
            {
                if ((Keyboard.IsKeyDown(Key.LeftShift) || Keyboard.IsKeyDown(Key.RightShift)) && e.Key.ToString().ToUpper() == Properties.Settings.Default.HelpHK)
                {
                    NIKernel.Instance.LoadPageView(Constants.PageViewID.HelpPageView);
                }
            }
            // Settings page hot key setup
            if (Properties.Settings.Default.SettingsHKM == "none")
            {
                if (e.Key.ToString().ToUpper() == Properties.Settings.Default.SettingsHK)
                {
                    NIKernel.Instance.LoadPageView(Constants.PageViewID.SettingsPageView);
                }
            }
            if (Properties.Settings.Default.SettingsHKM == "Ctrl")
            {
                if ((Keyboard.IsKeyDown(Key.LeftCtrl) || Keyboard.IsKeyDown(Key.RightCtrl)) && e.Key.ToString().ToUpper() == Properties.Settings.Default.SettingsHK)
                {
                    NIKernel.Instance.LoadPageView(Constants.PageViewID.SettingsPageView);
                }
            }
            if (Properties.Settings.Default.SettingsHKM == "Shift")
            {
                if ((Keyboard.IsKeyDown(Key.LeftShift) || Keyboard.IsKeyDown(Key.RightShift)) && e.Key.ToString().ToUpper() == Properties.Settings.Default.SettingsHK)
                {
                    NIKernel.Instance.LoadPageView(Constants.PageViewID.SettingsPageView);
                }
            }
        }
    }
}
