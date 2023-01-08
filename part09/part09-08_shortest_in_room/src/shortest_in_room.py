# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.persons = []
    
    def add(self,person: "Person"):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0

    def print_contents(self):
        total = 0
        for i in self.persons:
            total += i.height
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {total} cm")
        for i in self.persons:
            print(f"{i.name} ({i.height}cm)")
    
    def shortest(self):
        if len(self.persons) == 0:
            return None
        else:
            shrt_person= self.persons[0]
            shrt_height = self.persons[0].height
            for i in self.persons:
                if i.height < shrt_height:
                    shrt_height = i.height
                    shrt_person = i
            return shrt_person

    def remove_shortest(self):
        if len(self.persons) == 0:
            return None
        else:
            short = self.shortest()
            index = self.persons.index(short)
            return self.persons.pop(index)



if __name__ == "__main__":
    room = Room()
    print("Is the room empty?", room.is_empty())
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Ally", 166))
    room.add(Person("Nina", 162))
    room.add(Person("Dorothy", 155))
    print("Is the room empty?", room.is_empty())
    room.print_contents()
    room = Room()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))

    print()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    print()

    room.print_contents()
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
