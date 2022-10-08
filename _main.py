# This file is place where params and functions are called and combined together.
import user_input
import rand_airport
import current_gps
import current_time
import game_goal

name = user_input.get_user_name()
start_location = current_gps.get_chosen_airport_gps(rand_airport.get_random_airport())
start_time = current_time.get_init_time()
game_goal = game_goal.generate_game_goal()
new_airport = user_input.choose_your_destination()
