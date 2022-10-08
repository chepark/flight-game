# Show the following messages to a user
# 1)current_location
# 2) current_time
# 3) success_message
# 4) failure_message
# 5) game_over_message

current_location = "Helsinki_airport"
current_time = "8"
local_time = "5"
current_timezone = "Eastern_European_Summer_Time"
city = "Helsinki"


success_message=(f"Hooray! You are at {current_location} in {city}: "
                 f"The time zone is {current_time}: "
                 f"The local time is {local_time}:")

print(success_message)


#2
current_timezone = "Eastern European_Summer_Time"
local_time = "7"
airport_name = "Helsinki Airport"
city = "Helsinki"

failure_message = (f"sorry ! you are in the wrong timezone."
                   f"You arenot at the {airport_name} in {city}."
                   f"The timezone is {current_timezone} and the local time is {local_time}"
                   f"Please try again.")

print(failure_message)

#
total_timezone = "3"
total_airport = "5"
co2_budget = "100"

game_over_message = (f"Now, your co2 budget is over."
                     f"You have visited {total_timezone} and {total_airport}")

print(game_over_message)



