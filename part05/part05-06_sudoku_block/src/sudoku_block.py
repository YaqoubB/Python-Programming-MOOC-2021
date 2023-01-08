# Write your solution here

def block_correct(sudoku: list, row_no: int, column_no: int):
    list_1 = []
    new_list = []
    counter_1 = 0
    counter_2 = 0
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
    if len(new_list) < len(list_1):
        return False
    else:
        return True
        


if __name__ == "__main__":
    sudoku = [
        [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],   # row 0
        [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],   # row 1
        [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],   # row 2
        [ 2, 9, 4, 0, 0, 0, 4, 0, 0 ],   # row 3
        [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],   # row 4
        [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],   # row 5
        [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],   # row 6
        [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],   # row 7
        [ 3, 0, 1, 0, 0, 8, 0, 0, 2 ],   # row 8
        ]
    print(block_correct(sudoku, 0, 6))

