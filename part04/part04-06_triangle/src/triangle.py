# Copy here code of line function from previous exercise

def line(integer, character):
    if character == "":
        character = "*"
    character = character[0]
    print(character * integer)


def triangle(size):
    # You should call function line here with proper parameters
    counter = 0
    length = 1
    while counter < size:
        line(length, "#")
        counter += 1
        length += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
