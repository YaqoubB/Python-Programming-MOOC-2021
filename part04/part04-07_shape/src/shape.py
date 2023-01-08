# Copy here code of line function from previous exercise and use it in your solution

def line(integer, character):
    if character == "":
        character = "*"
    character = character[0]
    print(character * integer)

def shape(num1, str1, num2, str2):
    counter = 1
    index = 1
    while counter <= num1:
        line(counter, str1)
        counter += 1
    while index <= num2:
        line(num1, str2)
        index += 1
    



# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")