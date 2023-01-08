# Write your solution here

def who_won(game_board: list):
    player_1 = 0
    player_2 = 0
    for i in game_board:
        for j in i:
            if j == 1:
                player_1 += 1
            elif j == 2:
                player_2 += 1
    if player_1 > player_2:
        return 1
    elif player_1 < player_2:
        return 2
    elif player_1 == player_2:
        return 0


if __name__ == "__main__":
    m = [[1, 2, 0], [1, 0, 0], [1, 0, 0]]
    (who_won(m))

