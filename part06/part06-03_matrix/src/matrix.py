# write your solution here


def matrix_builder():
    matrix = []
    with open("matrix.txt") as new_file:
        for i in new_file:
            i = i.replace("\n", "")
            i = i.split(",")
            row = []
            for j in i:                     #i is now a list of strings taken from the first line of the matrix.txt
                row.append(int(j))              #integerizing each word in the string and adding to a empty row list
            matrix.append(row)                    #adding each row of list to the matrix list
            
    return matrix



def matrix_sum():
    matrix = matrix_builder()
    sum = 0
    for i in matrix:
        for j in i:
            sum += j
    return sum

def matrix_max():
    matrix = matrix_builder()

    max = 0
    for i in matrix:
        for j in i:
            if j > max:
                max = j
    return max

def row_sums():
    matrix = matrix_builder()

    row_list = []
    row_sum = 0
    for i in matrix:
        for j in i:
            row_sum += j
        row_list.append(row_sum)
        row_sum = 0
    return row_list


