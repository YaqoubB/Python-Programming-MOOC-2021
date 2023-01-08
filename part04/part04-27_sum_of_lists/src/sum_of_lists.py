# Write your solution here

def list_sum(list_1 : int, list_2 : int) -> int:
    counter = 0
    sum_list = []
    while counter < len(list_1):
        sum_list.append(list_1[counter] + list_2[counter])
        counter += 1
    return sum_list


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]

