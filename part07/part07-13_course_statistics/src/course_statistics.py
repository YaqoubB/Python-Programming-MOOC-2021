# Write your solution here

import urllib.request
import json



def retrieve_all():
    request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    my_request = request.read()
    content_1 = json.loads(my_request)
    content_2 = []
    content_3 = []
    for line in content_1:
        if line["enabled"] is True:
            content_2.append(line)
    for line in content_2:
        tuple_1 = (line["fullName"], line["name"], line["year"], sum(line["exercises"]))
        content_3.append(tuple_1)
        
    return content_3

def retrieve_course(course_name: str):
    request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    my_request = request.read()
    content_1 = json.loads(my_request)
    dictionary_1 = {}
    dictionary_1["weeks"] = len(content_1)
    biggest = 0
    hours_sum = 0
    excersie_sum = 0
    for i in content_1:  # i = 0,1,2,3
        if content_1[i]["students"] > biggest:
            biggest = content_1[i]["students"]
        hours_sum += content_1[i]["hour_total"]
        excersie_sum += content_1[i]["exercise_total"]      
    dictionary_1["students"] = biggest
    dictionary_1["hours"] = hours_sum
    dictionary_1["hours_average"] = hours_sum // biggest
    dictionary_1["exercises"] = excersie_sum
    dictionary_1["exercises_average"] = excersie_sum // biggest
    return dictionary_1
    



if __name__ == "__main__":
    retrieve_all()
    retrieve_course("docker2019")
