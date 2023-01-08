# WRITE YOUR SOLUTION HERE:


class Recording:
    def __init__(self, length: int):
        if length < 0:
            raise ValueError("The length must not be below zero")
        self.__length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length_set):
        if length_set < 0:
            raise ValueError("The length must not be below zero")
        self.__length = length_set