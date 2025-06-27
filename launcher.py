import requests

def get_weather(city=None):
    # 🔑 Replace with your actual OpenWeatherMap API key
    api_key = "1fe05b425e2a16b47c3868898c5a4ef6"

    # 1. Get current city using IP if not specified
    if not city:
        try:
            ip_info = requests.get("https://ipinfo.io/json").json()
            city = ip_info.get("city", "Chennai")
        except:
            city = "Chennai"

    # 2. Build API URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        # 3. Handle invalid city (e.g., misspelled)
        if data["cod"] != 200:
            return f"Deskie couldn't find weather for '{city}'. Please check the city name."

        # 4. Extract weather details
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        city_name = data["name"]

        return f"The current temperature in {city_name} is {temp}°C with {description}."

    except Exception as e:
        return f"Error getting weather: {str(e)}"
