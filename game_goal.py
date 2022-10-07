# 1) generate game goal
# - time zone limit ± X hours

from datetime import datetime, timedelta, time
import random
import current_time

#take initial time from current_time file
init_hour = current_time.init_hour
init_min = current_time.init_min

init_time = datetime.strptime(f"{init_hour}:{init_min}:00", "%H:%M:%S")


def generate_rand_time_dif():
    #generate random number to generate the goal
    random_dif =  (random.randint(-2, 2))

#calculating new goal time using datetime, timedelta
    if random_dif>0:
        delta = timedelta(hours=random_dif)
        new_goal = init_time + delta
        new_goal = new_goal.time().strftime('%H:%M')
        print(f"The new goal time is: {new_goal}")
        return new_goal

    elif random_dif<0:
        delta = timedelta(hours=random_dif)
        new_goal = init_time - delta
        new_goal = new_goal.time().strftime('%H:%M')
        print(f"The new goal time is: {new_goal}")
        return new_goal

    #in case random number equals 0, it is changed to 1
    elif random_dif ==0:
        random_dif = 1
        delta = timedelta(hours=random_dif)
        new_goal = init_time - delta
        new_goal = new_goal.time().strftime('%H:%M')
        print(f"The new goal time is: {new_goal}")
        return new_goal

def generate_game_goal():
    print(f"Choose the airport where the local time is: {new_goal}")

new_goal = generate_rand_time_dif()
generate_game_goal()




