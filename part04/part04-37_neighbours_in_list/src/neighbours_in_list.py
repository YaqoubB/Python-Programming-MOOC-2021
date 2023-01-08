# Write your solution here

def longest_series_of_neighbours(list :list) -> list:
    list_1 = []
    counter_1 = 0
    counter_2 = 1
    counter_3 = 0
    while counter_2 + 1 <= len(list):
        if (list[counter_1] - list[counter_2]) == 1 or (list[counter_1] - list[counter_2]) == -1:
            counter_3 += 1
            counter_1 += 1
            counter_2 += 1
            list_1.append(counter_3)
        else:
            counter_1 += 1
            counter_2 += 1
            list_1.append(counter_3)
            counter_3 = 0
    if len(list) == 2:
        return max(list_1)
    else:
        return (max(list_1) + 1)
    
if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))