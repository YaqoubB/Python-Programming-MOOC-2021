# Write your solution here

def row_sums(my_matrix: list):
    layer = len(my_matrix[0])
    sum = 0
    for i in my_matrix:
        for j in range(layer):
            sum += i[j]
        i.append(sum)
        sum = 0
