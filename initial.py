import requests
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Minimalistic Weather Environment")
city_label=tk.Label(root,  text="Would you like to know how to dress for the weather outside? \n Input your city:")
city_label.pack()
city_entry=tk.Entry(root)
city_entry.pack()
fetch_button=tk.Button(root, text="Fetch Weather Information")
fetch_button.pack()
weather_label=tk.Label(root, text="")
weather_label.pack()

def fetch_weather():
    city = city_entry.get()
    api_key = "b960c936c1f42f9d9eb23eb55d593b93"
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        temperature=data["main"]["temp"]
        weather=data["weather"][0]["description"]
        if ((temperature - 273.15)>30):{
            weather_label.config(text=f"Temperature: {(temperature - 273.15):.2f}°C\nWeather: {weather}\nWear light tops, shorts/skirts, and summer dresses; stay cool and don't forget about sunscreen :).")
        }
        if (25<=(temperature - 273.15)<30):{
            weather_label.config(text=f"Temperature: {(temperature - 273.15):.2f}°C\nWeather: {weather}\nLight clothing like T-shirts, shorts, or airy dresses work well; stay hydrated.")
        }
        if (20<=(temperature - 273.15)<25):{
            weather_label.config(text=f"Temperature: {(temperature - 273.15):.2f}°C\nWeather: {weather}\nComfortable in T-shirts and jeans or a light sweater; maybe a thin jacket at night.")
        }
        if (15<=(temperature - 273.15)<20):{
            weather_label.config(text=f"Temperature: {(temperature - 273.15):.2f}°C\nWeather: {weather}\nLayer with a long-sleeve top or sweater, add a light jacket; it can feel chilly.")
        }
        if (10<=(temperature - 273.15)<15):{
            weather_label.config(text=f"Temperature: {(temperature - 273.15):.2f}°C\nWeather: {weather}\nSweaters and medium jackets are best; add a scarf if you're sensitive to cold.")
        }
        if (5<=(temperature - 273.15)<10):{
            weather_label.config(text=f"Temperature: {(temperature - 273.15):.2f}°C\nWeather: {weather}\nLayer up with a thick sweater, coat, and maybe a hat; it feels damp.")
        }
        if (0<=(temperature - 273.15)<5):{
            weather_label.config(text=f"Temperature: {(temperature - 273.15):.2f}°C\nWeather: {weather}\nWear a warm coat, gloves, and scarf; add a hat and grab some hot coffee to stay cozy.")
        }
        if ((temperature - 273.15)<0):{
            weather_label.config(text=f"Temperature: {(temperature - 273.15):.2f}°C\nWeather: {weather}\nBundle up with a heavy winter coat, thermal layers, gloves, hat, and scarf; Poland’s humidity can make it feel even colder!")
        }
    except Exception as e:
        messagebox.showerror("Error", "Invalid city name or API limit reached.")
        print(e)

fetch_button.config(command=fetch_weather)

root.mainloop()