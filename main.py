from datetime import datetime
from weather_api import WeatherApi

def format_date(date):
    date_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    return date_obj.strftime("%a, %d %b %Y")

def get_weather(lat, lon, units):
    weather_api = WeatherApi(lat, lon, units)
    responses = weather_api.weather_forecast_for_five_days()
    weather_data = responses["list"]
    current_date = weather_data[0]["dt_txt"]
    current_hour = current_date.split(" ")[1]
    for weather in weather_data:        
        if current_hour in weather["dt_txt"]:
            formatted_date = format_date(weather["dt_txt"])
            temp = weather["main"]["temp"]
            print(f"{formatted_date}: {temp}{chr(176)}C")

if __name__ == "__main__":
    get_weather(-6.195527, 106.824474, "metric")