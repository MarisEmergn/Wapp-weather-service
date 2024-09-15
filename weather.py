import requests
from config import OPENWEATHERMAP_API_KEY

# Function to fetch weather data from OpenWeatherMap API
def get_weather_data(location):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            # Simplified weather data response
            weather_info = {
                'location': location,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'wind_speed': data['wind']['speed'],
                'humidity': data['main']['humidity']
            }
            return weather_info
        else:
            return None
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None
