import requests

API_KEY = "d51d90fab628a5916b6d0867d023cadc"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

lat = input("Enter a latitude: ")
lon = input("Enter a longitude: ")
request_url = f"{BASE_URL}?appid={API_KEY}&lat={lat}&lon={lon}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    description = data["weather"][0]["description"]
    temp = round(data["main"]["temp"] - 273.15, 2)
    print(
        f"For location lat-{lat}, long-{lon} \n{description}\nTemperature: {temp}")
else:
    print(response.status_code)
    print("An error occured")
