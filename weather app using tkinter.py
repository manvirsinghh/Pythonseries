import tkinter as tk
from tkinter import messagebox
import requests

# Function to get weather data
def get_weather():
    api_key = "64717c7434f24781bd962832251001"  # Replace with your actual API key
    city = city_entry.get()

    # Check if the city field is empty
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    # Weather API URL
    url =  f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"


    try:
        # Request the weather data
        response = requests.get(url)

        # If the response is OK (status code 200)
        if response.status_code == 200:
            data = response.json()  # Parse the JSON data

            # Extract weather information
            city_name = data["location"]["name"]
            temperature = data["current"]["temp_c"]
            description = data["current"]["condition"]["text"]

            # Display the weather data
            result_label.config(text=f"Weather in {city_name}:\n{description}\n{temperature}°C")
        else:
            # Show an error message if the city is not found
            messagebox.showerror("Error", "City not found.")
    
    except Exception as e:
        # Catch any errors (like network issues)
        messagebox.showerror("Error", str(e))

# Setting up the Tkinter window
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")

# City input label and entry
city_label = tk.Label(root, text="Enter City Name:")
city_label.pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

# Button to fetch weather
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

# Label to show the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
