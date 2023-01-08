# Write your solution here

def invert(dictionary: dict):
    my_dictionary = {}
    for i in dictionary:
        my_dictionary[dictionary[i]] = i
    dictionary.clear()
    for i in my_dictionary:
        dictionary[i] = my_dictionary[i]

        
if __name__ == "__main__":
    s = {1: 10, 2: 20, 3: 30}
    invert(s)
    print(s)