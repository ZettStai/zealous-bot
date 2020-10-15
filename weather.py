 # Given a string with multiple locations either city name or zip code or lat and lon (co-ordinates) find the hottest among the list

# Weather data info - https://openweathermap.org/current
# API - http://api.openweathermap.org/data/2.5/weather
# API token - 8aa28adc5d6dda1890f5a2b001a70ef8

# Example:
# Input - "92328,us;94105,us;Juneau;55.5,37.5"
# Expected Output - 92328,us

# (Need not be provided by us, the data info link above has this info)
# Useful APIs:
# Zip code: api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={your api key}
# City name: api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}
# By geographic coordinates: api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={your api key}

import re
import requests
import os

from dotenv import load_dotenv

load_dotenv()
APITOKEN = "d7457467f2492af08b5aa255be8b2e2e"

API = "http://api.openweathermap.org/data/2.5/weather"
    
def hotspot(locations):
    
    listofloc = locations.split(";")
    
    # expected listofloc ["94401,us","951345,us", "Juneau", "55.5,37.5"]
    
    #for each location in list
    
    
    for i in range(0, len(listofloc)):
        
        
        # Figure out if it is a zip, city, or coord
        
        # Check if zip code
        
        if re.search(r"^\d{5}", listofloc[i]) != None:
            zipcode = listofloc[i]
            zipreq = str(API) + "?zip=" + zipcode + "&appid=" + str(APITOKEN)
            
            print(zipreq)
    
        if re.search(r"^[A-Z][a-z]", listofloc[i]) != None:
            cityname = listofloc[i]
            cityreq = API + "?q=" + cityname + "&appid=" + APITOKEN
            print(cityreq)

        if re.search(r"\d+[.]\d", listofloc[i]) != None:
            coord = listofloc[i].split(",")
            lat = coord[0]
            lon = coord[1]
            coordreq = API + "?lat=" + lat + "&lon=" + lon + "&appid=" + APITOKEN
            print(lat)
            print(lon)
            print(coordreq)
        
        
        
        
# r = requests.get(zipreq) # temperature

# listoftemps 

# # Sort the list of temp

# listoftemps.sort()

# # Hottest temp

hotspot("95134,us;94401,us;48331,us;96797,us;Wattrelos;Asnières-sur-seine;78250,us")