# Write your solution here

def spruce(size):
    print("a spruce!")
    counter_1 = 1
    counter_2 = 1
    index = size
    while counter_1 < (size + 1):
        print(" " * (index - 1)+"*" * counter_2)
        counter_1 += 1
        counter_2 += 2
        index -= 1
    print(" " * (size - 1)+ "*")



# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)