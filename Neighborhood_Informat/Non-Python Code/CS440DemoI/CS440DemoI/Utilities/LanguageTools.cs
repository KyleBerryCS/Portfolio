using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CS440DemoI.Utilities
{
    class LanguageTools
    {
        public static void UpdateDisplayLanguage() {
            // Language settings for the main window
            NIKernel.Instance.MainWindow.Title = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.TitleEnglish : Properties.Settings.Default.TitleSpanish);
            // Language settings for the home page view
            NIKernel.Instance.HomePageView.SearchButton.ToolTip = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.HomeSearchBtnTTEnglish : Properties.Settings.Default.HomeSearchBtnTTSpanish);
            NIKernel.Instance.HomePageView.MapButton.ToolTip = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.HomeMapBtnTTEnglish : Properties.Settings.Default.HomeMapBtnTTSpanish);
            NIKernel.Instance.HomePageView.SettingsButton.ToolTip = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.HomeSettBtnTTEnglish : Properties.Settings.Default.HomeSettBtnTTSpanish);
            NIKernel.Instance.HomePageView.HelpButton.ToolTip = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.HomeHelpBtnTTEnglish : Properties.Settings.Default.HomeHelpBtnTTSpanish);
            // Language settings for the settings page view
            NIKernel.Instance.SettingsPageView.SettingsLabel.Content = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SettingsLabelEnglish : Properties.Settings.Default.SettingsLabelSpanish);
            NIKernel.Instance.SettingsPageView.EnglishRad.Content = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SettingsEngRadioEnglish : Properties.Settings.Default.SettingsEngRadioSpanish);
            NIKernel.Instance.SettingsPageView.SpanishRad.Content = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SettingSpaRadioEnglish : Properties.Settings.Default.SettingSpaRadioSpanish);
            NIKernel.Instance.SettingsPageView.LanguageGroupBox.Header = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SettingsLangGBHEnglish : Properties.Settings.Default.SettingsLangGBHSpanish);
            NIKernel.Instance.SettingsPageView.HotKeyGroupBox.Header = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SettingsHotKeyGBHEnglish : Properties.Settings.Default.SettingsHotKeyGBHSpanish);
            NIKernel.Instance.SettingsPageView.ApplyButton.Content = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SettingsApplyBtnEnglish : Properties.Settings.Default.SettingsApplyBtnSpanish);
            NIKernel.Instance.SettingsPageView.HKESearchLabel.Content = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SettingsHKESearchEnglish : Properties.Settings.Default.SettingsHKESearchSpanish);
            NIKernel.Instance.SettingsPageView.HKEHomeLabel.Content = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SettingsHKEHomeEnglish : Properties.Settings.Default.SettingsHKEHomeSpanish);
            NIKernel.Instance.SettingsPageView.HKEMapLabel.Content = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SettingsHKEMapEnglish : Properties.Settings.Default.SettingsHKEMapSpanish);
            NIKernel.Instance.SettingsPageView.HKEHelpLabel.Content = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SettingsHKEHelpEnglish : Properties.Settings.Default.SettingsHKEHelpSpanish);
            NIKernel.Instance.SettingsPageView.HKESettingsLabel.Content = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SettingsHKESettingsEnglish : Properties.Settings.Default.SettingsHKESettingsSpanish);
            // Language settings for the search page view
            NIKernel.Instance.SearchPageView.SearchByGroupBox.Header = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SearchByGBHEnglish : Properties.Settings.Default.SearchByGBHSpanish);
            NIKernel.Instance.SearchPageView.CommunityRadio.Content = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SearchCommRadioEnglish : Properties.Settings.Default.SearchCommRadioSpanish);
            NIKernel.Instance.SearchPageView.BlockRadio.Content = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SearchBlockRadioEnglish : Properties.Settings.Default.SearchBlockRadioSpanish);
            NIKernel.Instance.SearchPageView.ByStatRadio.Content = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SearchByStatRadioEnglish : Properties.Settings.Default.SearchByStatRadioSpanish);
            NIKernel.Instance.SearchPageView.CurrentSearchGroupBox.Header = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SearchCurrentGBHEnglish : Properties.Settings.Default.SearchCurrentGBHSpanish);
            NIKernel.Instance.SearchPageView.SaveCurrentButton.Content = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SearchSaveCurBtnEnglish : Properties.Settings.Default.SearchSaveCurBtnSpanish);
            NIKernel.Instance.SearchPageView.LoadCurrentButton.Content = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SearchLoadCurBtnEnglish : Properties.Settings.Default.SearchLoadCurBtnSpanish);
            NIKernel.Instance.SearchPageView.ExportSearchGroupBox.Header = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SearchExportGBHEnglish : Properties.Settings.Default.SearchExportGBHSpanish);
            NIKernel.Instance.SearchPageView.ExportSeachButton.Content = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SearchExportBtnEnglish : Properties.Settings.Default.SearchExportBtnSpanish);
            NIKernel.Instance.SearchPageView.ImportSearchButton.Content = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SearchImportBtnEnglish : Properties.Settings.Default.SearchImportBtnSpanish);
            NIKernel.Instance.SearchPageView.ResultsLabel.Content = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SearchResultsLabelEnglish : Properties.Settings.Default.SearchResultsLabelSpanish);
            NIKernel.Instance.SearchPageView.RefineSeachGroupBox.Header = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SearchRefineGBHEnglish : Properties.Settings.Default.SearchRefineGBHSpanish);
            NIKernel.Instance.SearchPageView.AdvancedExpander.Header = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SearchExpanderHEnglish : Properties.Settings.Default.SearchExpanderHSpanish);
            NIKernel.Instance.SearchPageView.ShowTopLabel.Content = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.SearchShowTopTBEnglish : Properties.Settings.Default.SearchShowTopTBSpanish);
            // Language settings for the help page view
            
            // Language settings for the map page view
            NIKernel.Instance.MapPageView.MapLabel.Content = (Properties.Settings.Default.IsInEnglish == true ? Properties.Settings.Default.MapMapLabelEnglish : Properties.Settings.Default.MapMapLabelSpanish);
        }
    }
}
