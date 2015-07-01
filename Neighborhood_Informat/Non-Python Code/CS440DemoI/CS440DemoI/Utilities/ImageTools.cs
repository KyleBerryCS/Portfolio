using System;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media.Imaging;

namespace CS440DemoI.Utilities
{
    class ImageTools
    {
        public static Image SetButtonImage(string Path)
        {
            Image image = new Image();
            image.Margin = new Thickness(20);
            BitmapImage bi = new BitmapImage();
            bi.BeginInit();
            bi.UriSource = new Uri(Path, UriKind.RelativeOrAbsolute);
            bi.DecodePixelWidth = 300;
            bi.EndInit();
            image.Source = bi;
            return image;
        }

        public static Image SetButtonImage(string Path, int PixelWidth)
        {
            Image image = new Image();
            image.Margin = new Thickness(20);
            BitmapImage bi = new BitmapImage();
            bi.BeginInit();
            bi.UriSource = new Uri(Path, UriKind.RelativeOrAbsolute);
            bi.DecodePixelWidth = PixelWidth;
            bi.EndInit();
            image.Source = bi;
            return image;
        }

        public static Image SetButtonImage(string Path, int PixelWidth, int Width, int Height)
        {
            Image image = new Image();
            image.Margin = new Thickness(20);
            BitmapImage bi = new BitmapImage();
            bi.BeginInit();
            bi.UriSource = new Uri(Path, UriKind.RelativeOrAbsolute);
            bi.DecodePixelWidth = PixelWidth;
            bi.EndInit();
            image.Source = bi;
            image.Width = Width;
            image.Height = Height;
            return image;
        }
    }
}
