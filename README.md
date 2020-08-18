# Selenium-based-Zerochan-Image-Downloader
An image downloader for [Zerochan](https://zerochan.net/)

## Setup
If you don't have Selenium installed, download it [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) based on your Chrome version.
Be sure to put "chromedriver.exe" in C:\Program Files(x86)\.

## Explanation
This doesn't use Selenium as a downloader, but rather only uses it to get the links. 
If you don't care about having an account and don't want a browser to be deployed, [this](https://github.com/HarvyJC/Zerochan-Image-Downloader) would work too.
This program uses Selenium to access the website, BeautifulSoup to get the links, and wget to download each image.
