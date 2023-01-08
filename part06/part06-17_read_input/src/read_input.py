# Write your solution here


def read_input(request :str, low :int, high:int):
    while True:
        try:
            answer = input(request)
            answer = int(answer)
            if  low < answer < high:
                return answer
        except ValueError:
            pass
        print("You must type in an integer between 5 and 10")
          







if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)