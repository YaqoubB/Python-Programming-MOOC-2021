# Write your solution here

def double_items(numbers: list):
    list_1 = []
    for i in numbers:
        list_1.append(i * 2)
    return list_1






if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)