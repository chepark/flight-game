# 1) get the longitude and latitude of the current airport 
# - use DB

import mysql.connector

airport_latitude = 0
airport_longitude = 0
# get latitude and longitude from player's current airport and chosen airport
def get_chosen_airport_gps(airport_name):
    sql = "SELECT name, latitude_deg, longitude_deg FROM Airport"
    sql += " WHERE name ='" + airport_name + "'"
    global airport_latitude
    global airport_longitude
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"This is {row[0]} airport, which has latitude is {row[1]} and longitude is {row[2]}.")
            airport_latitude = row[1]
            airport_longitude = row[2]
    return [row[1], row[2]]


# Main program
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game2',
         user='root',
         password='manager',
         autocommit=True
         )
# Player enter airport name to get data of latitude and longitude

"""
current_airport = input("Enter airport name: ")
current_location = get_chosen_airport_gps(current_airport)
print(current_location)

chosen_airport = input("Enter the name of airport that you want to go from the list: ")
new_location = get_chosen_airport_gps(chosen_airport)
print(new_location)
"""