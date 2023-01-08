# Write your solution here

def column_correct(sudoku: list, column_no: int):
    list_1 = []
    for i in sudoku:
        index = i[column_no]
        list_1.append(index)
    list_1 = sorted(list_1)
    new_list = []
    while 0 in list_1:
        list_1.remove(0)
    for i in list_1:
        if i not in new_list:
            new_list.append(i)
    if len(new_list) < len(list_1):
        return False
    else:
        return True



if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]
    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))

