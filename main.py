from urllib.request import urlopen
import urllib.parse
import json
import time


class Helper:
    def __init__(self):
        pass

    # converts the kelvin temperature returned from the api to farenheit
    def temp_conversion(self, temperature):
        converted = 1.8 * (float(temperature) - 273) + 32
        return int(converted)

    def time_conversion(self, api_time):
        return time.strftime("%I:%M %p", time.localtime(int(api_time)))



key = "22330685c3be7c2bd44f391522a4f8b0"
cityName = "Simi Valley"

nameEncoded = urllib.parse.quote(cityName)

url = f"http://api.openweathermap.org/data/2.5/weather?q={nameEncoded}&appid={key}"

util = Helper()

with urlopen(url) as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data, indent=2))

currentTemp = util.temp_conversion(data["main"]["temp"])
sunrise = util.time_conversion(int(data["sys"]["sunrise"]))
sunset = util.time_conversion(int(data["sys"]["sunset"]))

lowTemp = util.temp_conversion(data["main"]["temp_min"])
highTemp = util.temp_conversion(data["main"]["temp_max"])
