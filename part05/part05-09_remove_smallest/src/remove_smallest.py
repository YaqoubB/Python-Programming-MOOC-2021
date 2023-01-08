# Write your solution here

def remove_smallest(numbers: list):
    list_1 = sorted(numbers [:])
    smallest = list_1[0]
    numbers.remove(smallest)



if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)