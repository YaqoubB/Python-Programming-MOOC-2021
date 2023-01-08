# Write your solution here

def play_turn(game_board: list, x: int, y: int, piece: str):
    if x < 0 or x >= 3:
        return False
    if y < 0 or y >= 3:
        return False
    if game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    else:
        return False





if __name__ == "__main__":
    game_board = [['', 'X', 'X'], ['O', '', 'X'], ['', '', '']]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)