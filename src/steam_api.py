import requests
from pprint import pprint


url = "https://steamcommunity.com/inventory/76561198230023632//730/2?l=english&count=5000"

#float_url = "https://csfloat.com/api/v1/listings"

response = requests.get(url)


pprint(response.json())