# weatherscraper
Detects the user's location using their IP address and fetches real-time weather data, including maximum and minimum temperatures and weather conditions, from OpenWeatherMap.

1. Detecting User Location using Geolocation

    The script uses the geocoder library to determine the user's city and country based on their IP address.
    The function get_user_location() calls geocoder.ip("me"), which queries an external service to retrieve the approximate geographic location of the device running the script.
    If the geolocation request succeeds, the function returns the detected city and country.
    If geolocation fails (e.g., due to network issues or API restrictions), a fallback default location is set to Rochester, US to ensure the script continues functioning.

2. Fetching Real-Time Weather Data using OpenWeatherMap API

    The function fetch_weather_data(city, country) takes the detected (or default) city and country as input.
    It constructs an API request URL for OpenWeatherMap, incorporating the user's location and an API key (OPENWEATHER_API_KEY).
    The request is sent using the requests library to retrieve weather data in JSON format.

3. Extracting and Displaying Weather Data

    If the API request is successful (status_code == 200), the script extracts the following weather details from the JSON response:
        Maximum temperature (temp_max)
        Minimum temperature (temp_min)
        Weather description (e.g., "clear sky", "rainy", etc.)
    The extracted information is displayed in a user-friendly format, including temperature readings in Celsius and a capitalized weather description.

4. Error Handling for API Requests

    If the API request fails, the script prints an error message with the HTTP status code and the response text to help debug the issue.
    This ensures the script does not crash when the API is unavailable, the location is invalid, or the API key is incorrect.

5. Integration of Multiple Programming Concepts

    Geolocation: Uses the geocoder library to detect the user's location automatically.
    HTTP Requests & APIs: Sends an HTTP GET request to OpenWeatherMap and retrieves structured JSON data.
    JSON Parsing: Extracts specific weather details from the API response.
    Error Handling: Handles potential failures from geolocation detection and API requests.
    String Formatting & User-Friendly Output: Formats temperature values and weather descriptions before displaying them.
