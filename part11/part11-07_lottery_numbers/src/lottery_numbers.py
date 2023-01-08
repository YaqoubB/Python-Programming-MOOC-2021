# WRITE YOUR SOLUTION HERE:


class LotteryNumbers:
    def __init__(self, week: int, lotto_list: list):
        self.week = week
        self.lotto_list = [number for number in lotto_list if type(number) == int]

    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.lotto_list])

    def hits_in_place(self, numbers: list):
        return [numbers[i] if numbers[i] in self.lotto_list else -1 for i in range(len(numbers))]