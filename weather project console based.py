import requests  # Import the requests library

# Define the URL of the API endpoint (WeatherAPI)
api_key = "64717c7434f24781bd962832251001"  # Replace with your WeatherAPI API key
city = "manali"  # Example city
base_url = "http://api.weatherapi.com/v1/current.json"  # Correct endpoint for WeatherAPI

# Complete URL to make the GET request
url = f"{base_url}?key={api_key}&q={city}"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract relevant information from the response
    city_name = data["location"]["name"]
    temperature = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    description = data["current"]["condition"]["text"]
    wind_speed = data["current"]["wind_kph"]
    
    # Display the extracted data
    print(f"Weather for {city_name}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {description.capitalize()}")
    print(f"Wind Speed: {wind_speed} km/h")

else:
    # If the response was not successful, print an error message
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
