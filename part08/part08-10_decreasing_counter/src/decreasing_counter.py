# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.original = initial_value


    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value >= 1:
            self.value -= 1


    # Write the rest of the methods here!

    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.original





if __name__ == "__main__":
    counter = DecreasingCounter(2)
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.decrease()
    counter.print_value()
    counter.reset_original_value