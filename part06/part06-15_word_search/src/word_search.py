# Write your solution here

def find_words(search_term: str):
    word_list = []
    contents = []
    counter = 0
    with open("words.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            contents.append(line)
    if "*" not in search_term and "." not in search_term:
        if search_term in contents:
            word_list.append(search_term)
    if search_term.find("*") == 0:
        for i in contents:
            if i.endswith(search_term[1:]) is True:
                word_list.append(i)
    if search_term.find("*") > 0:
        for i in contents:
            if i.startswith(search_term[:-1]) is True:
                word_list.append(i)
    if search_term.find(".") > 0:
        for i in contents:
            if len(i) == len(search_term):
                for j in range(len(search_term)):
                    if i[j] == search_term[j] or search_term[j] == ".":
                        counter += 1
                    else:
                        counter = 0
                        break
                    if counter == len(search_term):  
                        word_list.append(i)
                        counter = 0

    
    return word_list
    



if __name__ == "__main__":
    print(find_words("reson*"))