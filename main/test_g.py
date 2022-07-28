import os
import googlemaps
import requests
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()
GMAPS_API = os.environ['GMAPS_API']
gmaps = googlemaps.Client(key=GMAPS_API)


# Just testing the various functionalities that I might need in aws and gcp
l_x ='31.959733'
l_y = '35.861790'
l_t ='256 Zahran St'

nearby_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={l_x}%2C{l_y}&rankby=distance&key={GMAPS_API}"
payload={}
headers = {}

nearby_result = requests.request("GET", nearby_url, headers=headers, data=payload)


geocode_result = gmaps.geocode(l_t)
reverse_geocode_result = gmaps.reverse_geocode(f"{l_x},{l_y}")

print(nearby_result.text)

# print(reverse_geocode_result)
# print(geocode_result)
# print(nearby_result.text)