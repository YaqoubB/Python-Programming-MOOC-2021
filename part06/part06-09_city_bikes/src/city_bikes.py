# tee ratkaisu tänne
# Write your solution here

import math


def get_station_data(filename: str):
    location_dictionary = {}
    with open(filename) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            line = line.split(";")
            for word in line:
                if line[0] == "Longitude":
                    continue
                else:
                    location_dictionary[line[3]] = ( float(line[0]) , float(line[1]) )
    return location_dictionary


def distance(stations: dict, station1: str, station2: str):
    longitude1 = stations[station1][0]
    longitude2 = stations[station2][0]
    latitude1 = stations[station1][1]
    latitude2 = stations[station2][1]
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    key_list = list(stations.keys())
    furthest = 0
    counter = 0 
    for i in key_list:
        for j in range(len(key_list)-1):
            dist = distance(stations, i, key_list[1 + j])
            if dist > furthest:
                station_1 = i
                station_2 = key_list[1 + j]
                furthest = dist            
    return (station_1, station_2, furthest)




if __name__ == "__main__": 
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)

    #stations = get_station_data('stations1.csv')
    #for key, value in stations.items():
        #print(key,value)
    #d = distance(stations, "Designmuseo", "Hietalahdentori")
    #print(d)
    #d = distance(stations, "Viiskulma", "Kaivopuisto")
    #print(d)