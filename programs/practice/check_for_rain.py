# Chapter 20 - Sending Emails, Texts and Push notifications
# (Practice Program) - Umbrella Reminder

import os
import requests
from dotenv import load_dotenv


BASE_URL = "https://api.weatherapi.com/v1/forecast.json"


def main():
    # Load environment variables
    load_dotenv()

    # Ask user for location
    location = "Toronto"

    # Request 1-day forecast
    params = {
        "key": os.getenv('NTFY_API_KEY'),
        "q": location,
        "days": 1,
        "aqi": "no",
        "alerts": "no"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        print("Error:", data.get("error", {}).get("message", "Unknown error"))
    else:
        location_name = data['location']['name']
        country = data['location']['country']
        current = data['current']
        forecast_day = data['forecast']['forecastday'][0]

        # Print basic weather info
        message = f"""
        Weather for {location_name}, {country}
    - Temperature: {current['temp_c']}°C
    - Condition: {current['condition']['text']}
    - Humidity: {current['humidity']}%
    - Wind: {current['wind_kph']} km/h
    """

        # Check if rain is expected
        will_it_rain_today = forecast_day['day']['daily_will_it_rain']
        chance_of_rain = forecast_day['day']['daily_chance_of_rain']

        if will_it_rain_today:
            title = f"Rain is expected today! (Chance: {chance_of_rain}%)"
            tags = "rain,umbrella,cloud"
        else:
            title = f"No rain expected today"
            tags = "sunny,sunglasses"
        
        response = requests.post(
            url=os.getenv('RAIN_URL'),
            data=message.encode("utf-8"),
            headers={
                "Title": title,
                "Tags": tags
            }
        )


if __name__ == "__main__":
    main()