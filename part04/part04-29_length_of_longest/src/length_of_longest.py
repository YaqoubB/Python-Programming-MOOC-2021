# Write your solution here

def length_of_longest(list : str) -> str:
    best = 0
    for i in list:
        if len(i) > best:
            best = len(i) 
    return best

if __name__ == "__main__":
    my_list = ['Alan', 'Grace', 'Frances', 'Kim', 'Susan']
    result = length_of_longest(my_list)
    print(result)