# 1) Co2 budget
# 2) Calculate Co2 level left
# - return Co2 level left

# Calculate the distance between current location and new location of the player

from geopy.distance import geodesic as GD

# import function from current_gps file
from current_gps import *

co2_budget = 600
co2_consumed_per_km = 0.115
visited_airport_count = 0

# The player is relocated by the game
current_airport = input("Enter airport name: ")
current_location = get_chosen_airport_gps(current_airport)
#print(current_location)

# Player can fly as many times as there is available CO2 budget left. Using while loop to iterate the flight action
while co2_budget > 0:
    chosen_airport = input("Enter the name of airport that you want to go from the list: ")
    new_location = get_chosen_airport_gps(chosen_airport)
    #print(new_location)
    visited_airport_count += 1

    # calculate distance between two airports
    print(f"The distance between current airport and {chosen_airport} is: ", GD(current_location, new_location).km)
    distance = GD(current_location, new_location).km

    # calculate CO2 consumed and available CO2 budget left
    co2_consumed_per_flight = distance * co2_consumed_per_km
    co2_budget = co2_budget - co2_consumed_per_flight

    if co2_budget < 0:
        print("Your CO2 budget is not enough to fly")
        break
    # updating new location of player after each flight

    current_location[0] = new_location[0]
    current_location[1] = new_location[1]
    print(f"Your flight from current airport to {chosen_airport} consumed: {co2_consumed_per_flight} kg of CO2")
    print(f"Your CO2 budget left is: {co2_budget} kg")
print(f"The number of airport you have visited is: {visited_airport_count}")

























