# Write your solution here

def sudoku_grid_correct(sudoku: list):
    counter = 0
    row_1 = 0
    column_1 = 0
    while counter < 8:
        if row_correct(sudoku, counter) and column_correct(sudoku, counter) is True:
            counter += 1
        else:
            return False
    while row_1 <= 6:
        while column_1 <= 6:
            if block_correct(sudoku, row_1 , column_1) is True:
                column_1 += 3
            else:
                return False
        row_1 += 3
        coulumn_1 = 0
    return True


def row_correct(sudoku: list, row_no: int):
    list_1 = sorted(sudoku[row_no])
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
        list_1 = []
        new_list = []
        return False
    else:
        list_1 = []
        new_list = []
        return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    row_no = 0
    column_no = 0
    list_1 = []
    new_list = []
    counter_1 = 0
    counter_2 = 0
    while row_no <= 6:
        while column_no <= 6:
            while counter_1 < 3:
                while counter_2 < 3:
                    add_column = sudoku[row_no + counter_2][column_no + counter_1]
                    list_1.append(add_column)
                    counter_2 += 1
                counter_1 += 1
                counter_2 = 0    
            while 0 in list_1:
                list_1.remove(0)
            for i in list_1:
                if i not in new_list:
                    new_list.append(i)
            if len(new_list) != len(list_1):
                return False
            list_1 = []
            new_list = []
            column_no += 3
            counter_1 = 0
        list_1 = []
        new_list = []
        row_no += 3
        counter_1 = 0
        column_no = 0
    return True


if __name__ == "__main__":
    sudoku1 = [
        [ 2, 9, 5, 0, 8, 4, 7, 1, 3 ],
        [ 6, 4, 8, 1, 3, 7, 9, 2, 5 ],
        [ 1, 7, 3, 2, 0, 9, 4, 6, 8 ],
        [ 8, 6, 0, 3, 4, 1, 2, 5, 7 ],
        [ 5, 2, 7, 8, 9, 6, 0, 3, 4 ],
        [ 3, 1, 4, 0, 7, 2, 6, 8, 9 ],
        [ 7, 5, 0, 9, 2, 8, 1, 4, 0 ],
        [ 4, 3, 6, 7, 1, 5, 8, 0, 2 ],
        [ 0, 8, 0, 4, 6, 3, 5, 7, 1 ],
        ]
    print(sudoku_grid_correct(sudoku1))