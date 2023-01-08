# Write your solution here

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    list_1 = sudoku[0][:]
    list_2 = sudoku[1][:]
    list_3 = sudoku[2][:]
    list_4 = sudoku[3][:]
    list_5 = sudoku[4][:]
    list_6 = sudoku[5][:]
    list_7 = sudoku[6][:]
    list_8 = sudoku[7][:]
    list_9 = sudoku[8][:]
    list_a = [list_1, list_2, list_3, list_4, list_5, list_6, list_7, list_8, list_9]
    list_a[row_no][column_no] = number
    return list_a

def print_sudoku(sudoku: list):
    counter_1 = 0
    counter_2 = 0
    for i in sudoku:
        for j in i:
            counter_1 += 1
            if j > 0:
                print(f"{j}", end="")
                if counter_1 < 9:
                    print(" ", end="")
            else:
                print("_", end="")
                if counter_1 < 9:
                    print(" ", end="")
            if counter_1 == 3:
                print(f" ", end="")
            if counter_1 == 6:
                print(f" ", end="")
        counter_1 = 0
        counter_2 += 1
        print()
        if counter_2 == 3:
            print()
        if counter_2 == 6:
            print()



if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)