
import user_data

def success(): 
    success_message=(f"\nHooray! You made it.")
    print(success_message)


def fail(time_gap): 
    failure_message = (f"\nSorry! You are in the wrong time zone." 
                    f"\nThe time gap between {user_data.current_airport} and {user_data.new_location} is {time_gap} hour(s)."
                    f"\nPlease try again.")
    print(failure_message)

def game_over():
    game_over_message = (f"Now, your co2 budget is over."
                        f"You have visited {user_data.total_visited_airports} airports.")
    print(game_over_message)
