# Write your solution here:

class Item:
    def __init__(self, name : str, weight: int):
        if name != "":
            self.__name = name
        if weight >= 0:
            self.__weight = weight
    
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.inside = []

    def weight(self):
        total_weight = 0
        for i in self.inside:
            total_weight += i.weight()
        return int(total_weight)
    
    def quantity(self):
        return len(self.inside)

    def add_item(self, item: Item):
        if self.weight() + item.weight() < self.max_weight:
            self.inside.append(item)
    
    def __str__(self):
        if self.quantity() == 1:
            return f"{self.quantity()} item ({self.weight()} kg)"
        return f"{self.quantity()} items ({self.weight()} kg)"

    def print_items(self):
        for i in self.inside:
            print(i)
    
    
    def heaviest_item(self):
        if self.quantity() == 0:
            return None
        else:
            heaviest = self.inside[0]
            for i in self.inside:
                if i.weight() > heaviest.weight():
                    heaviest = i
            return heaviest

class CargoHold:
    def __init__(self, maximum_weight):
        self.maximum_weight = maximum_weight
        self.inside = []
    

    def current_weight(self):
        total_weight = 0
        for i in self.inside:
            total_weight += i.weight()
        return total_weight


    def remaining_weight(self):
        return self.maximum_weight - self.current_weight()

    def add_suitcase(self, suitcase: Suitcase):
        if self.remaining_weight() >= suitcase.weight():
            self.inside.append(suitcase)


    def __str__(self):
        if len(self.inside) == 1:
            return f"{len(self.inside)} suitcase, space for {self.remaining_weight()} kg"
        return f"{len(self.inside)} suitcases, space for {self.remaining_weight()} kg"

    def print_items(self):
        for suitcase in self.inside:
            for item in suitcase.inside:
                print(item)


if __name__ == "__main__":
    '''book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)

    print("Name of the book:", book.name())
    print("Weight of the book:", book.weight())

    print("Book:", book)
    print("Phone:", phone)

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(5)
    print(suitcase)

    suitcase.add_item(book)
    print(suitcase)

    suitcase.add_item(phone)
    print(suitcase)

    suitcase.add_item(brick)
    print(suitcase)
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    print("The suitcase contains the following items:")
    suitcase.print_items()
    combined_weight = suitcase.weight()
    print(f"Combined weight: {combined_weight} kg")

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    heaviest = suitcase.heaviest_item()
    print(f"The heaviest item: {heaviest}")

    cargo_hold = CargoHold(1000)
    print(cargo_hold)

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold.add_suitcase(adas_suitcase)
    print(cargo_hold)

    cargo_hold.add_suitcase(peters_suitcase)
    print(cargo_hold)

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()'''

    suitcase = Suitcase(25)
    item = Item("ABC Book", 2)
    suitcase.add_item(item)
    suitcase.weight()