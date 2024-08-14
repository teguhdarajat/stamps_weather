import os
import requests
from dotenv import load_dotenv

class WeatherApi:
    
    def __init__(self, lat, lon, units):
        load_dotenv()
        self.base_url = os.getenv("BASE_URL") 
        self.api_key = os.getenv("API_KEY")
        self.lat = lat
        self.lon = lon
        self.units = units
        
    def weather_forecast_for_five_days(self):
        url = f"{self.base_url}/data/2.5/forecast?lat={self.lat}&lon={self.lon}&units={self.units}&appid={self.api_key}"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"RequestException Error: {err}")
        
        return response.json()
