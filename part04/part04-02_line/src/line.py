# Write your solution here
# You can test your function by calling it within the following block

def line(integer, character):
    if character == "":
        character = "*"
    character = character[0]
    print(character * integer)



if __name__ == "__main__":
    line(5, "x")