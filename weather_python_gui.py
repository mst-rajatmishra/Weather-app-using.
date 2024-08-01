import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city):
    api_key = "2f1d45ccd17ae38a000ed1a43a0a2315"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url +"q=" + city + "&appid=" + api_key

    response = requests.get(complete_url)
    data=response.json()

    if data["cod"] !="404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"] - 273.15
        humidity = main["humidity"]
        description = weather["description"]


        weather_info = f"Temperature: {temperature:.2f}°C\n"
        weather_info += f"Humidity: {humidity}%\n"
        weather_info += f"Description: {description.capitalize()}"
        
        return weather_info
    else:
        return "City not found"
    

def display_weather():
    city = city_entry.get()
    if city:
        weather_info = get_weather(city)
        weather_label.config(text=weather_info)
    else:
        messagebox.showerror("Error", "City field cannot be empty")
    


root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")

city_label = tk.Label(root, text="Enter City Name")
city_label.pack()


city_entry = tk.Entry(root)
city_entry.pack()

Show_weather_button = tk.Button(root, text="Show Weather", command=display_weather)
Show_weather_button.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()

root.mainloop()

