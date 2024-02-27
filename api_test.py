import requests
api_key = "30d4741c7"
user_input= "https://www.weatherapi.com/weather/q/rangoon-1576335"
response= requests.get(user_input)
weather_data=response.json()
if response.status_code == 200:

    temperature = weather_data["main"]["temp"]
    temp_in_C = round(temperature - 273.15,2)
    temp_in_F = round((temperature * 9 / 5) +32,2)

    description = weather_data["weather"][0]["description"]
    print(f"Current weather in {user_input},Temperature : {temp_in_F} or {temp_in_C}")
else : print("Error")
