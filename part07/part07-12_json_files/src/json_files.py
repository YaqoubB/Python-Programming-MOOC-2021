# Write your solution here

import json

def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()
    content = json.loads(data)
    for line in content:
        name = line["name"]
        age = line["age"]
        hobbies = line["hobbies"]
        hobby_1 = ""
        for i in hobbies:
            hobby_1 += i+", "   
        hobby_2 = f"({hobby_1[:-2]})"   
        print(name, age, "years", hobby_2)

if __name__ == "__main__":
    print_persons("file1.json")