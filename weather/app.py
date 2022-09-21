import requests
from dotenv import load_dotenv, dotenv_values

# Load environmental variables
load_dotenv()
env_variables = dotenv_values(".env")

API_KEY = env_variables["API_KEY"]
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Get user input
lat = input("Enter a latitude: ")
lon = input("Enter a longitude: ")

# Make API requests
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
