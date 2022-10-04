import random
# 1) airport list

airports = ["Amsterdam Airport Schiphol", "Berlin Brandenburg Airport", "Charles de Gaulle International Airport",
            "Copenhagen Kastrup Airport", "Dublin Airport", "Geneva Cointrin International Airport", "Gran Canaria Airport",
            "Helsinki Vantaa Airport", "Lennart Meri Tallinn Airport", "Lviv International Airport",
            "London Gatwick Airport",  "Luxembourg-Findel International Airport", "Milan Bergamo Airport",  "Oslo Airport",
            "Gardermoen", "Riga International Airport", "Sheremetyevo International Airport", "Vilnius International Airport",
            "Warsaw Chopin Airport", "Zagreb Airport"]

# 2) generate random airport to begin the game
def get_random_airport():
    airport = random.choice(airports)
    #to check the amount of airports in the list
    #print("Number of items in the list = ", len(airports))
    return airport

get_random_airport()