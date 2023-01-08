# Write your solution here
def chessboard(length):
    counter = 0
    word = "10" * length
    while counter < length:
        print(f"{word[0:length]}")
        counter += 1
        if counter < length:
            print(f"{word[1:length+1]}")
            counter += 1


# Testing the function
if __name__ == "__main__":
    chessboard(13)

