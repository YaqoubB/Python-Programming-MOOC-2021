# Write your solution here

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




def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

if __name__ == "__main__":
    sudoku = [
        [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
        [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
        [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
        [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
        [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
        [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
        [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
        [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
        [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],
        ]
    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)