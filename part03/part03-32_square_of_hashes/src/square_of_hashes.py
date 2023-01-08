# Write your solution here
def hash_square(length):
    counter = 0
    while counter < length:
        print("#" * (length))
        counter += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)