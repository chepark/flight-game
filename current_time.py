# 1) calculate the current time of the location 
# - use longitude, latitude, and time API
import requests
import json

airport_latitude = 0
airport_longitude = 0

response = requests.get(f'https://timeapi.io/api/Time/current/coordinate?latitude={airport_latitude}&longitude={airport_longitude}').json()
#print(response)


init_time = (response["time"])
print(f"The time in the beginning of the game is: {init_time}")


