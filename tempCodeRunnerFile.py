from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root. geometry("900x500")
root.resizable(False,False)

def getWeather():
    try:
        city=textfield.get()
        geolocator= Nominatim(user_agent="geoapiExercises")
        location= geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name. config(text="CURRENT WEATHER")

        #weather
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&&appid=d16822bea18ea176c1dc2ad35ef75b4a"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"º"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"º"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    
    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!")