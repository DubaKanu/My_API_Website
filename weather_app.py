import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"  # Use Celsius
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"Weather in {city}: {data['weather'][0]['description'].capitalize()}")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Humidity: {data['main']['humidity']}%")
        else:
            print(f"Error: {data['message']}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    city = input("Enter the city name: ")
    get_weather(city)
