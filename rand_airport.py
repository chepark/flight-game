# 1) airport list
# 2) generate random airport to begin the game

import random

airports = ["Amsterdam Airport Schiphol", "Berlin Brandenburg Airport", "Charles de Gaulle International Airport",
            "Copenhagen Kastrup Airport", "Dublin Airport", "Funchal", "Geneva Cointrin International Airport", "Gran Canaria Airport",
            "Helsinki Vantaa Airport", "Ittoqqortoormiit", "Jan Mayensfield","Lennart Meri Tallinn Airport", "Lviv International Airport",
            "London Gatwick Airport",  "Luxembourg-Findel International Airport", "Milan Bergamo Airport","Minsk National Airport",  "Oslo Airport",
            "Ponta Delgada", "Pulkovo Airport", "Gardermoen", "Riga International Airport", "Sheremetyevo International Airport", "Vilnius International Airport",
            "Warsaw Chopin Airport", "Zagreb Airport"]

#list of airports to start the game
starting_point = ["Berlin Brandenburg Airport","Geneva Cointrin International Airport", "Milan Bergamo Airport"]

#3 lists of airports for a user to choose from, each list consists of 5 airports and each airport is
#in different time zone

airport_list1 = ["Ponta Delgada", "London Gatwick Airport","Oslo Airport","Helsinki Vantaa Airport", "Sheremetyevo International Airport"]
airport_list2 = ["Jan Mayensfield", "Funchal","Amsterdam Airport Schiphol", "Lennart Meri Tallinn Airport","Minsk National Airport" ]
airport_list3 =["Ittoqqortoormiit", "Gran Canaria Airport","Warsaw Chopin Airport","Lviv International Airport", "Pulkovo Airport"]
lists_of_airports = ([airport_list1],[airport_list2],[airport_list3])

#returns a starting point airport
def get_random_airport():
    current_airport = random.choice(starting_point)
    return current_airport

#generates lists of airports to choose from
def generate_answer_options():
    random_num =  (random.randint(1, 3))
    answer_options = 1
    if random_num == 1:
        answer_options = airport_list1
    elif random_num == 2:
        answer_options = airport_list2
    elif random_num == 3:
        answer_options = airport_list3
    #print(f"Choose the airport from the list: {answer_options}")
    return answer_options

#print(get_random_airport())

