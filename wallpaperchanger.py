import os
import subprocess
import sys
import time
import urllib.request
import winreg
from datetime import datetime

import requests

api_key_openweathermap = "your_api"
api_key_unsplash = "your_api"
location = "your_city"

month = datetime.now().month
if month in [12, 1, 2]:
    season = "winter"
elif month in [3, 4, 5]:
    season = "spring"
elif month in [6, 7, 8]:
    season = "summer"
else:
    season = "autumn"

image_path = os.path.join(os.path.expanduser("~"), "Pictures", "background.jpg")

while True:
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key_openweathermap}&units=metric"
    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()
    temperature = weather_data["main"]["temp"]

    image_url = f"https://api.unsplash.com/photos/random?query={season}+world&orientation=landscape&client_id={api_key_unsplash}"
    if temperature < 0:
        image_url += "&color=blue"
    elif temperature < 12:
        image_url += "&color=green"
    else:
        image_url += "&color=yellow"
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        image_data = image_response.json()
        image_url = image_data["urls"]["full"]

        urllib.request.urlretrieve(image_url, image_path)

        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, "Wallpaper", 0, winreg.REG_SZ, image_path)

        subprocess.call("RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters ,1 ,True", shell=True)
        time.sleep(5)
        break
    else:
        print(f"Failed to download image. Status code: {image_response.status_code}. Retrying in 5 seconds...")
        time.sleep(5)

task_name = "ChangeWallpaper"
powershell_exe = sys.executable.replace("python.exe", "powershell.exe")
cmd_args = f"-ExecutionPolicy Bypass -File '{os.path.abspath(__file__)}'"
cmd = f"{powershell_exe} {cmd_args}"
subprocess.run(f"schtasks /create /tn {task_name} /tr \"{cmd}\" /sc onstart /ru {os.getlogin()} /f", shell=True)

print("Wallpaper successfully changed.")
sys.exit(0)