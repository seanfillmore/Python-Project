from tkinter import *


def get_weather():
    weather_function()


# tkinter GUI
root = Tk()

root.title("Weather")
root.geometry("500x250")

city_text = StringVar()
city_label = Label(root, text="City Name", font=("bold", 14), padx=10)
city_label.grid(row=0, column=0)
city_entry = Entry(root, textvariable=city_text)
city_entry.grid(row=0, column=1)

weather_btn = Button(root, text="Get Weather", width=12, command=get_weather)
weather_btn.grid(row=0, column=2)

sunrise_label = Label(root, text=f"Sunrise will be {sunrise}", padx=10)
sunrise_label.grid(row=1, column=0, columnspan=6, sticky=W)

sunset_label = Label(root, text=(f"Sunset will be {sunset}"), padx=10)
sunset_label.grid(row=2, column=0, columnspan=6, sticky=W)

lowTemp_label = Label(root, text=(f"The low will be {lowTemp} degrees"), padx=10)
lowTemp_label.grid(row=3, column=0, columnspan=6, sticky=W)

highTemp_label = Label(root, text=f"The high will be {highTemp} degrees", padx=10)
highTemp_label.grid(row=4, column=0, columnspan=6, sticky=W)

currentTemp_label = Label(
    root, text=f"The current temperature is {currentTemp} degrees", padx=10
)
currentTemp_label.grid(row=5, column=0, columnspan=6, sticky=W)


root.mainloop()
