import requests
import geocoder  # Library to get user's location

# 🔑 Replace this with your OpenWeatherMap API Key
OPENWEATHER_API_KEY = "a0087c3701cf2c954d203def8f6c6e44"

def get_user_location():
    """Automatically detect user's city and country using IP."""
    g = geocoder.ip("me")  # Get location from IP
    if g.ok:
        return g.city, g.country
    else:
        print("Failed to detect location. Using default: Rochester, US")
        return "Rochester", "US"

def fetch_weather_data(city: str, country: str):
    """Fetch real-time weather data from OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&units=metric&appid={OPENWEATHER_API_KEY}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp_max = data["main"]["temp_max"]
        temp_min = data["main"]["temp_min"]
        weather_desc = data["weather"][0]["description"]

        print(f"🌍 Location: {city}, {country}")
        print(f"🌡️ Max Temp: {temp_max}°C | Min Temp: {temp_min}°C")
        print(f"⛅ Condition: {weather_desc.capitalize()}")
    else:
        print(f"❌ Failed to retrieve weather data: {response.status_code} - {response.text}")

# 🔎 Auto-detect user location
city, country = get_user_location()

# 🌤️ Fetch real-time weather for detected location
fetch_weather_data(city, country)
