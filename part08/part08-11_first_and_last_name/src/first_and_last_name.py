# Write your solution here:

class Person:
    def __init__(self, name: str):
        self.name = name

    def return_first_name(self):
        name1 = self.name
        name1 = name1.split()
        return name1[0]

    def return_last_name(self):
        name2 = self.name
        name2 = name2.split()
        return name2[1]












