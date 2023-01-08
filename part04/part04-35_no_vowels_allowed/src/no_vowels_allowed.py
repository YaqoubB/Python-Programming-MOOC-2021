# Write your solution here

def no_vowels(string_1 :str) -> str: 
    string_new = string_1
    for i in string_new:
        if i == "a" or i == "e" or i == "i" or i =="o" or i == "u":
            string_new = string_new.replace(i, "")
    return string_new




if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))