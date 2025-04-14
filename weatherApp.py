wimport requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io

def get_weather(city):
    api_key = 'd6b1377bde26a469fc276ec2dd366e7c'  # Replace with your OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Will raise HTTPError for bad responses
        data = response.json()
        return data
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            messagebox.showerror("Error", "City not found. Please enter a valid city name.")
        else:
            messagebox.showerror("Error", f"HTTP Error: {err}")
    except requests.exceptions.RequestException as err:
        messagebox.showerror("Error", f"Request Error: {err}")
    return None

def display_weather():
    city = city_entry.get()
    weather_data = get_weather(city)

    if weather_data:
        city_name = weather_data['name']
        temperature = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        icon_code = weather_data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"

        # Update GUI labels
        city_label.config(text=f"City: {city_name}")
        temp_label.config(text=f"Temperature: {temperature}°C")
        desc_label.config(text=f"Weather: {weather_description.capitalize()}")
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_label.config(text=f"Wind Speed: {wind_speed} m/s")

        # Update weather icon
        icon_response = requests.get(icon_url)
        icon_data = icon_response.content
        icon_image = Image.open(io.BytesIO(icon_data))
        icon_photo = ImageTk.PhotoImage(icon_image)
        icon_label.config(image=icon_photo)
        icon_label.image = icon_photo
    else:
        city_label.config(text="")
        temp_label.config(text="")
        desc_label.config(text="")
        humidity_label.config(text="")
        wind_label.config(text="")
        icon_label.config(image="")

# Setup Tkinter window
root = tk.Tk()
root.title("Weather App")

# City input
city_entry = tk.Entry(root)
city_entry.pack(pady=10)

# Get weather button
get_weather_btn = tk.Button(root, text="Get Weather", command=display_weather)
get_weather_btn.pack(pady=5)

# Weather info labels
city_label = tk.Label(root, text="", font=('bold', 14))
city_label.pack()

temp_label = tk.Label(root, text="")
temp_label.pack()

desc_label = tk.Label(root, text="")
desc_label.pack()

humidity_label = tk.Label(root, text="")
humidity_label.pack()

wind_label = tk.Label(root, text="")
wind_label.pack()

# Weather icon label
icon_label = tk.Label(root, image=None)
icon_label.pack(pady=10)

root.mainloop()
