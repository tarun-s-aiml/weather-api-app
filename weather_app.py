import requests

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        print("\n===== WEATHER INFORMATION =====")
        print("City        :", data["name"])
        print("Temperature :", data["main"]["temp"], "°C")
        print("Feels Like  :", data["main"]["feels_like"], "°C")
        print("Humidity    :", data["main"]["humidity"], "%")
        print("Wind Speed  :", data["wind"]["speed"], "m/s")
        print("Condition   :", data["weather"][0]["description"].title())

    except requests.exceptions.HTTPError:
        print("City not found or API request failed.")

    except requests.exceptions.RequestException:
        print("Unable to connect to the weather service.")


print("===== WEATHER APP =====")

city = input("Enter city name: ").strip()

if city:
    get_weather(city)
else:
    print("Please enter a city name.")
