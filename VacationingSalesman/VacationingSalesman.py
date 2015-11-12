import json, urllib, requests
from haversine import haversine

def salesman(file_name):
    #Checks whether the user wants distances in kilometers or miles
    km_or_mi = input('Would you like distances in (km) or (mi)? ')
    if km_or_mi == "km":
        mile = False
        unit = " kilometers"
    else: 
        mile = True
        unit = " miles"

    locations = []
    #Reads text file and puts the locations into a list
    locations = open(file_name).read().splitlines()
    ind_distances = []
    total_distance = 0

    #Checks if there is at least two locations to travel between
    if len(locations) > 1:
        #Loop through all locations starting from the second location
        for index in range(len(locations)-1):
            start =  locations[index]
            end =  locations[index+1]
            #Finds the distane between the start and ending locations
            path_distance = find_distance(start, end, mile)
            #Save the indiviudal distances traveled
            ind_distances.append(path_distance)

            total_distance += path_distance
        #Checks if any distance was actually traveled
        if total_distance > 0:
            print("Success! Your vacation intinerary is:")
            #Prints out the individual legs and distances
            for i in range(len(locations)-1):
                print(str(locations[i]) + " -> " + str(locations[i+1]) + " : " + "%.2f" % round(ind_distances[i],2) + unit)
            print("Total distance covered in your trip: " + "%.2f" % round(total_distance,2) + unit)
        else:
            print("Oops! Please double check your intinerary to make sure you're traveling to new locations.")
    else:
        print("Oops! Please double check your intinerary to make sure you're traveling to new locations.")





def find_distance(start, end, miles=True):

    response1 = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+start)
    response2 = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+end)
    resp_json_payload1 = response1.json()
    resp_json_payload2 = response2.json()

    #Retrieve latitude and longitude of the starting and ending points
    orig_lat = resp_json_payload1['results'][0]['geometry']['location']['lat']
    orig_lon = resp_json_payload1['results'][0]['geometry']['location']['lng']
    dest_lat = resp_json_payload2['results'][0]['geometry']['location']['lat']
    dest_lng = resp_json_payload2['results'][0]['geometry']['location']['lng']

    orig_coord = (orig_lat, orig_lon)
    dest_coord = (dest_lat, dest_lng)
    #Find the distance between the starting and ending points using the Haversine equation
    distance_traveled = haversine(orig_coord, dest_coord, miles)
    

    # url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&language=en-EN&units=imperial".format(str(orig_coord),str(dest_coord))
    # result = requests.get(url)
    # resp_json = result.json()
    # distance_traveled= resp_json['rows'][0]['elements'][0]['distance']['text']

    return distance_traveled



