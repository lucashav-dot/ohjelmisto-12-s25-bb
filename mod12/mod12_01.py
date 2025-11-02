import json
import requests


# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyyntö = "https://api.chucknorris.io/jokes/random"


try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()

        print(json_vastaus['value'])
        #for a in json_vastaus:
            #print(a["show"]["name"])
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")
    print(e)