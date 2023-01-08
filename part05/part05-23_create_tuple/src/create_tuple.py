# Write your solution here


def create_tuple(x: int, y: int, z: int):
    list_1 = [x, y, z]
    list_1.sort()
    sum = 0
    for i in list_1:
        sum += i
    x = list_1[0]
    y = list_1[-1]
    z = sum
    tuple_1 = (x, y, z)
    return tuple_1

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))