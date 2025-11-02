import json
import requests
API_key = "f05a79882d93a8805199b8463ad4caba"
city_name = input("anna kaupungin nimi: ")
lang = "fi"

pyyntö = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang={lang}"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        data = vastaus.json()

        print(f"sää kohteessa {city_name} on {data["weather"][0]["description"]}, {data["main"]["temp"]}°C")


except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")
    print(e)
