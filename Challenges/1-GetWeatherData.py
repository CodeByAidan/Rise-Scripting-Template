import requests


def get_weather(city: str) -> str:
    """
    Challenge 1 - Get Weather Data

    This function retrieves weather data for a given city using the OpenWeatherMap API.

    Args:
        city (str): The name of the city for which to retrieve weather data.

    Returns:
        str: A string containing the weather information for the given city.
    """
    API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key - https://home.openweathermap.org/api_keys
    # API URL for weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    # Send request to the API
    response = requests.get(url, timeout=5)

    # Parse response and extract weather information
    if response.status_code == 200:
        data = response.json()
        weather_info = ...
        # Extract relevant weather data (e.g., temperature, description)
        # Return weather information
        return "Weather information for " + city + ":\n" + weather_info
    else:
        return "Error: Unable to retrieve weather data"


# Test the function
city_name = "New York"
weather = get_weather(city=city_name)
print(weather)
