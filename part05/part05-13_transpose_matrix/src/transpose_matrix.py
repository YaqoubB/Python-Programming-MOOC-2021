# Write your solution here

def transpose(matrix: list):
    list_1 = []
    for i in matrix:
        list_1.append(i[:])
        
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = list_1[j][i]



if __name__ == "__main__":
    matrix = [[1, 2], [1, 2]]
    transpose(matrix)