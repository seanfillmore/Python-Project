from urllib.request import urlopen
import urllib.parse
import tkinter as tk
import json
import time

# ----------Dictionary is used to hold the values retrieved from the API
weather_Dict = {
    "currentTemp": "",
    "sunrise": "",
    "sunset": "",
    "lowTemp": "",
    "highTemp": "",
}


class Helper:
    def __init__(self):
        pass

    # --------converts the kelvin temperature returned from the api to farenheit
    def temp_conversion(self, temperature):
        converted = (temperature - 273.15) * 9 / 5 + 32
        return int(converted)

    # --------converts the returned time to local time
    def time_conversion(self, api_time):
        return time.strftime("%I:%M %p", time.localtime(int(api_time)))


# --------Makes the API call and retrieves the data
def get_weather(city_name):
    key = "22330685c3be7c2bd44f391522a4f8b0"
    cityName = city_name

    # --------Encodes the city name to account for any white space
    nameEncoded = urllib.parse.quote(cityName)

    url = f"http://api.openweathermap.org/data/2.5/weather?q={nameEncoded}&appid={key}"

    util = Helper()

    with urlopen(url) as response:
        source = response.read()

    data = json.loads(source)

    weather_Dict["currentTemp"] = util.temp_conversion(data["main"]["temp"])
    weather_Dict["sunrise"] = util.time_conversion(int(data["sys"]["sunrise"]))
    weather_Dict["sunset"] = util.time_conversion(int(data["sys"]["sunset"]))
    weather_Dict["lowTemp"] = util.temp_conversion(data["main"]["temp_min"])
    weather_Dict["highTemp"] = util.temp_conversion(data["main"]["temp_max"])

    # ------Can be used to check the json data

    # print(json.dumps(data, indent=2))
    return weather_Dict


# --------tkinter GUI---------
root = tk.Tk()

root.title("Weather")
root.geometry("500x200")

# -------Functions------------


def populate_weather():

    get_weather(str(city_text.get()))

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


# -------------City label and input---------------

city_text = tk.StringVar()
city_label = tk.Label(root, text="City Name", font=("bold", 14), padx=10)
city_label.grid(row=0, column=0)
city_entry = tk.Entry(root, textvariable=city_text)
city_entry.grid(row=0, column=1)

# -------------Weather Button---------------

weather_btn = tk.Button(root, text="Get Weather", width=12, command=populate_weather)
weather_btn.grid(row=0, column=2)

root.mainloop()
