# WRITE YOUR SOLUTION HERE:

class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        common = my_list[0]
        for i in my_list:
            if my_list.count(i) > my_list.count(common):
                common = i 
        return common

    
    @classmethod
    def doubles(cls, my_list: list):
        counter = 0
        exact = []
        exact.append(my_list[0])
        if my_list.count(my_list[0]) >= 2:
            counter += 1
        for i in my_list:
            if my_list.count(i) >= 2 and i not in exact:
                exact.append(i)
                counter += 1
        return counter
