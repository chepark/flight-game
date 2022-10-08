# THIS IS THE FILE WHERE ALL LOGICS ARE COMBINED TOGETHER.
import user_data
from user_input import *
from rand_airport import *
from current_gps import *
from current_time import *
from game_goal import * 
import co2
import message
from lib import *

if user_data.total_trials == 0:
    # RESET user_data
    user_data.name = get_user_name()
    user_data.co2_budget = 600
    user_data.total_visited_airports = 0
    user_data.current_airport = get_random_airport()

def play_game():
    airport_gps = get_chosen_airport_gps(user_data.current_airport)
    airport_time = get_airport_time(airport_gps[0], airport_gps[1])
    goal = generate_game_goal(airport_time)
    
    # GET THE USER ANSWER
    user_data.new_location = choose_your_destination()
    
    new_location_gps = get_chosen_airport_gps(user_data.new_location)
    new_location_time = get_airport_time(new_location_gps[0], new_location_gps[1])

    # CHECK IF USER ANSWER IS CORRECT
    new_location_hour = int(new_location_time['hour'])
    goal_hour = get_hour(goal)

    if new_location_hour == goal_hour:
        message.success()
    else:
        time_gap = goal_hour - new_location_hour 
        message.fail(time_gap)
    
    # CALCULATE CO2
    co2.calculate_co2()

while user_data.co2_budget > 0: 
    play_game()