# Copy here code of line function from previous exercise

def line(integer, character):
    if character == "":
        character = "*"
    character = character[0]
    print(character * integer)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    counter = 0
    while counter < size:
        line(size, "#")
        counter += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
