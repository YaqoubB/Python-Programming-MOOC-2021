# Write your solution here

layers = int(input("Layers: "))

matrix = int((layers * 2) - 1)

dictionary = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H", 9:"I", 10:"J", 11:"K", 12:"L", 13:"M", 14:"N", 15:"O", 16:"P", 17:"Q", 18:"R", 19:"S", 20:"T", 21:"U", 22:"V", 23:"W", 24:"X", 25:"Y", 26:"Z"}

list_1 = [] 

def make_matrix(list_1):
    for i in range(matrix):
        list_1.append([])
    for i in range(matrix):
        for j in range(matrix):
            list_1[i].append(0)
    return list_1      

def fill_matrix(list_1):
    counter_1 = 0
    counter_2 = layers
    while counter_2 > 0:
        for i in range(0 + counter_1, len(list_1) - counter_1):
            for j in range(0 + counter_1, len(list_1[i]) - counter_1):
                list_1[i][j] = dictionary[layers - counter_1]
        counter_1 += 1
        counter_2 -= 1
    
def print_matrix(list_1):
    for i in list_1:
        for j in i:
            print(f"{j}", end="")
        print()
    



make_matrix(list_1)
fill_matrix(list_1)
print_matrix(list_1)