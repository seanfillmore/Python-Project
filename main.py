from urllib.request import urlopen
from urllib.error import HTTPError
from tkinter import messagebox
import urllib.parse
import tkinter as tk
import os
import json
import time

weather_Dict = {
    "currentTemp": "",
    "sunrise": "",
    "sunset": "",
    "lowTemp": "",
    "highTemp": "",
}

data = {}

key = os.environ.get("OPENWEATHER_API")


def kelvin_to_farenheit_conversion(temperature):
    converted = (temperature - 273.15) * 9 / 5 + 32
    return int(converted)


def unix_to_local_time_conversion(api_time):
    return time.strftime("%I:%M %p", time.localtime(int(api_time)))


def populate_weather(city_name):

    url_encoded_city_name = urllib.parse.quote(city_name)

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={url_encoded_city_name}&appid={key}"

        with urlopen(url) as response:
            source = response.read()

    except HTTPError:
        tk.messagebox.showwarning(
            title="Warning", message="Check your city name and try again."
        )
    except Exception as e:
        tk.messagebox.showwarning(title="Warning", message=f"Something went wrong! {e}")
    else:

        data = json.loads(source)

        weather_Dict["currentTemp"] = kelvin_to_farenheit_conversion(
            data["main"]["temp"]
        )
        weather_Dict["sunrise"] = unix_to_local_time_conversion(
            int(data["sys"]["sunrise"])
        )
        weather_Dict["sunset"] = unix_to_local_time_conversion(
            int(data["sys"]["sunset"])
        )
        weather_Dict["lowTemp"] = kelvin_to_farenheit_conversion(
            data["main"]["temp_min"]
        )
        weather_Dict["highTemp"] = kelvin_to_farenheit_conversion(
            data["main"]["temp_max"]
        )

        sunrise_label = tk.Label(
            master=root, text=f"Sunrise will be {weather_Dict['sunrise']}", padx=10
        )
        sunrise_label.grid(row=1, column=0, columnspan=6, sticky=tk.W)

        sunset_label = tk.Label(
            master=root, text=(f"Sunset will be {weather_Dict['sunset']}"), padx=10
        )
        sunset_label.grid(row=2, column=0, columnspan=6, sticky=tk.W)

        lowTemp_label = tk.Label(
            master=root,
            text=(f"The low will be {weather_Dict['lowTemp']} degrees"),
            padx=10,
        )
        lowTemp_label.grid(row=3, column=0, columnspan=6, sticky=tk.W)

        highTemp_label = tk.Label(
            master=root,
            text=f"The high will be {weather_Dict['highTemp']} degrees",
            padx=10,
        )
        highTemp_label.grid(row=4, column=0, columnspan=6, sticky=tk.W)

        currentTemp_label = tk.Label(
            master=root,
            text=f"The current temperature is {weather_Dict['currentTemp']} degrees",
            padx=10,
        )
        currentTemp_label.grid(row=5, column=0, columnspan=6, sticky=tk.W)


def get_weather():
    city_name = city_text.get()

    populate_weather(city_name)


# --------tkinter GUI---------
root = tk.Tk()

root.title("Weather")
root.geometry("500x200")

city_text = tk.StringVar()
city_label = tk.Label(root, text="City Name", font=("bold", 14), padx=10)
city_label.grid(row=0, column=0)
city_entry = tk.Entry(root, textvariable=city_text)
city_entry.grid(row=0, column=1)

weather_btn = tk.Button(root, text="Get Weather", width=12, command=get_weather)
weather_btn.grid(row=0, column=2)

root.mainloop()
