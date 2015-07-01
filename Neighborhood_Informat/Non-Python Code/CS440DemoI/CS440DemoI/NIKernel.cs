using System;
using System.Collections.Generic;
using System.Windows;

namespace CS440DemoI
{
    public class NIKernel
    {
        /* The crimes database link: */
        /* https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2 */

        private static NIKernel instance;

        private NIKernel() { }

        public static NIKernel Instance
        {
            get
            {
                if (instance == null)
                {
                    instance = new NIKernel();
                }
                return instance;
            }
        }

        private Window mainWindow;
        public Window MainWindow
        {
            get { return mainWindow; }
        }

        private Views.HomePageView homePageView;
        public Views.HomePageView HomePageView
        {
            get { return homePageView; }
        }
        private Views.SearchPageView searchPageView;
        public Views.SearchPageView SearchPageView
        {
            get { return searchPageView; }
        }
        private Views.HelpPageView helpPageView;
        public Views.HelpPageView HelpPageView
        {
            get { return helpPageView; }
        }
        private Views.SettingsPageView settingsPageView;
        public Views.SettingsPageView SettingsPageView
        {
            get { return settingsPageView; }
        }
        private Views.MapPageView mapPageView;
        public Views.MapPageView MapPageView
        {
            get { return mapPageView; }
        }

        internal Database.DBInstance DBInstance;

        public void InitNIKernel(Window MainWindow) {
            this.mainWindow = MainWindow;

            this.PopulateDatabaseInstance();

            this.homePageView = new Views.HomePageView();
            this.searchPageView = new Views.SearchPageView();
            this.helpPageView = new Views.HelpPageView();
            this.settingsPageView = new Views.SettingsPageView();
            this.mapPageView = new Views.MapPageView();
            
            Utilities.LanguageTools.UpdateDisplayLanguage();

            this.LoadPageView(Constants.PageViewID.HomePageView);
        }

        public void LoadPageView(Constants.PageViewID PageViewID)
        {
            switch (PageViewID)
            {
                case Constants.PageViewID.HomePageView:
                    this.mainWindow.Content = this.homePageView;
                    break;
                case Constants.PageViewID.SearchPageView:
                    this.mainWindow.Content = this.searchPageView;
                    NIKernel.Instance.SearchPageView.ShowTopTextBox.Text = Properties.Settings.Default.SearchShowTopValue;
                    break;
                case Constants.PageViewID.HelpPageView:
                    this.mainWindow.Content = this.helpPageView;
                    break;
                case Constants.PageViewID.SettingsPageView:
                    this.mainWindow.Content = this.settingsPageView;
                    break;
                case Constants.PageViewID.MapViewPage:
                    this.mainWindow.Content = this.mapPageView;
                    break;
                default:
                    this.mainWindow.Content = this.homePageView;
                    break;
            }
        }

        private void PopulateDatabaseInstance()
        {
            this.DBInstance = new Database.DBInstance();
        }
    }
}
