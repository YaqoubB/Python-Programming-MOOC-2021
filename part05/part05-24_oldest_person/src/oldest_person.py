# Write your solution here

def oldest_person(people: list):
    oldest = int(people[0][1])
    name_oldest = people[0][0]
    for i in people:
        if int(i[1]) < oldest:
            oldest = i[1]
            name_oldest = i[0]
    return name_oldest



if __name__ == "__main__":
    people = [("Arthur", 1977), ("Emily", 2014)]
    print(oldest_person(people))