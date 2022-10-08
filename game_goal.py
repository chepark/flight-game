# 1) generate game goal
# - time zone limit ± X hours
#use "generate_game_goal" to generate first time goal
#use "generate_random_timegoal" in other cases, later in the game
#actually you can use just "generate_random_timegoal", it is new and should't have issues of
#"generate_game_goal", which is to go out of our range

from datetime import datetime, timedelta, time
import random
import current_time

#take initial time from current_time file
init_hour = current_time.init_hour
init_min = current_time.init_min

init_time = datetime.strptime(f"{init_hour}:{init_min}:00", "%H:%M:%S")

def list_of_time_goals():
    time1 = init_time + timedelta(hours=2)
    time1 = time1.time().strftime('%H:%M')
    time2 = init_time + timedelta(hours=1)
    time2 = time2.time().strftime('%H:%M')
    time3 = init_time + timedelta(hours=0)
    time3 = time3.time().strftime('%H:%M')
    time4 = init_time - timedelta(hours=1)
    time4 = time4.time().strftime('%H:%M')
    time5 = init_time - timedelta(hours=2)
    time5 = time5.time().strftime('%H:%M')
    list_of_time = [time1,time2,time3,time4,time5]
    return list_of_time

#this function is used to generate time goal within our limit
def generate_random_timegoal ():
    time_goal = random.choice (list_of_time_goals())
    print(f"Find in which airort the time is: {time_goal}")


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

    elif random_dif<=0:
        delta = timedelta(hours=random_dif)
        new_goal = init_time - delta
        new_goal = new_goal.time().strftime('%H:%M')
        print(f"The new goal time is: {new_goal}")
        return new_goal


#this function can be used only in the beginning! because +2/-2 can end up out of our current range
def generate_game_goal():
    print(f"Choose the airport where the local time is: {generate_rand_time_dif()}")


#generate_game_goal()



