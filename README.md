# Wallpaper Changer Script
This script allows you to automatically change your desktop wallpaper based on the current season and temperature in your location (city must be specified). I personally created it to change wallpapers after booting up Windows 10 (by adding it to system startup). It has not been tested on other OS and is not planned to be tested.

## Usage
1. Download the script and open it with any text editor of your choice.
2. Install the latest version of Python from [python.org](https://www.python.org/downloads/)
3. In the `location = "your_city"` line, replace `your_city` with the full name of your city in Latin letters.
4. Get your API key from [openweathermap.org](https://openweathermap.org/) as follows:
   * Register on the [openweathermap.org](https://openweathermap.org/) website.
   * Click on your nickname in the upper right corner of the page and go to the `My API keys` section.
   * Generate a new API key with any name.
   * Copy the key and paste it into the `api_key_openweathermap = "your_api"` line instead of `your_api`.
5. Get your API key from [unsplash.com](https://unsplash.com/) as follows:
   * Register on the [unsplash.com](https://unsplash.com/) website.
   * Click on the `View more links` button (represented by three horizontal bars) in the upper right corner of the page, go to the `Developers/API` section.
   * Click `Your Apps`, then `New Application`.
   * Agree to everything, specify any name and description, and complete the app creation process.
   * Go to your app page, copy the Access Key, and paste it into the `api_key_unsplash = "your_api"` line instead of `your_api`.
6. Save the changes in the script.

Now you can run the script in a way that is convenient for you.
