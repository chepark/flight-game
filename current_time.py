# 1) calculate the current time of the location 
# - use longitude, latitude, and time API
import requests
import json
from datetime import datetime
import current_gps

airport_latitude = 0
airport_longitude = 0

def get_init_time():
    response = requests.get(f'https://timeapi.io/api/Time/current/coordinate?latitude={airport_latitude}&longitude={airport_longitude}').json()
    init_hour = (response["hour"])
    init_min = (response["minute"])
    init_time = datetime.strptime(f"{init_hour}:{init_min}:00", "%H:%M:%S")
    init_time = init_time.time().strftime("%H:%M")
    print(f"The time in the beginning of the game is: {init_time}")
    return init_time

response = requests.get(f'https://timeapi.io/api/Time/current/coordinate?latitude={airport_latitude}&longitude={airport_longitude}').json()
init_hour = (response["hour"])
init_min = (response["minute"])
