from tkinter import *
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500")
root.resizable(False, False)

def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        label_name.config(text="CURRENT WEATHER")

        # Weather API
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ce87df0a3927a6962b20d16a5cc71378"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        temperature_label.config(text=f"{temp}º")
        condition_label.config(text=f"{condition} | FEELS LIKE {temp}º")
        wind_label.config(text=wind)
        humidity_label.config(text=humidity)
        description_label.config(text=description)
        pressure_label.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!")

title_label = Label(root, text="Weather Forecast", font=("Arial", 24, "bold"), fg="#0066CC")
title_label.place(x=40, y=30)

search_image = PhotoImage(file=r"search.png")
search_label = Label(image=search_image)
search_label.place(x=350, y=20)

textfield = Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#434343", border=0, fg="white")
textfield.place(x=450, y=40)
textfield.focus()

search_icon = PhotoImage(file=r"search_icon.png")
search_button = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#434343", command=getWeather)
search_button.place(x=730, y=34)

logo_image = PhotoImage(file=r"logo.png")
logo_label = Label(image=logo_image)
logo_label.place(x=150, y=100)

frame_image = PhotoImage(file=r"box.png")
frame_label = Label(image=frame_image)
frame_label.pack(padx=5, pady=5, side=BOTTOM)

label_name = Label(root, font=("Arial", 15, "bold"))
label_name.place(x=30, y=100)

clock = Label(root, font=("Arial", 20))
clock.place(x=30, y=130)

label_wind = Label(root, text="WIND", font=("Arial", 15, 'bold'), fg="white", bg="#1ab5ef")
label_wind.place(x=120, y=400)

label_humidity = Label(root, text="HUMIDITY", font=("Arial", 15, 'bold'), fg="white", bg="#1ab5ef")
label_humidity.place(x=225, y=400)

label_description = Label(root, text="DESCRIPTION", font=("Arial", 15, 'bold'), fg="white", bg="#1ab5ef")
label_description.place(x=430, y=400)

label_pressure = Label(root, text="PRESSURE", font=("Arial", 15, 'bold'), fg="white", bg="#1ab5ef")
label_pressure.place(x=650, y=400)

temperature_label = Label(root, font=("Arial", 70, "bold"), fg="#ee666d")
temperature_label.place(x=400, y=150)

condition_label = Label(root, font=("Arial", 15, 'bold'))
condition_label.place(x=400, y=250)

wind_label = Label(root, font=("Arial", 20, "bold"), bg="#1ab5ef")
wind_label.place(x=120, y=430)

humidity_label = Label(root, font=("Arial", 20, "bold"), bg="#1ab5ef")
humidity_label.place(x=280, y=430)

description_label = Label(root, font=("Arial", 20, "bold"), bg="#1ab5ef")
description_label.place(x=450, y=430)

pressure_label = Label(root, font=("Arial", 20, "bold"), bg="#1ab5ef")
pressure_label.place(x=670, y=430)

root.mainloop()
