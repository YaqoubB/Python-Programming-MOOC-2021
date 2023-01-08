# Write your solution here



def search_by_name(filename: str, word: str):
    new_list_1 = []
    recipes_list = []
    recipes_list_2 = []
    with open(filename) as new_file:
        for line in new_file:
            new_list_1.append(line)
        recipes_list.append(new_list_1[0])
        counter = 0
        for i in new_list_1:
                if i == "\n":
                    recipes_list.append(new_list_1[counter + 1])
                counter += 1
    for i in range(len(recipes_list)):
        recipes_list[i] = recipes_list[i][:-1]  
    for i in recipes_list:
        if word in i.lower():
            recipes_list_2.append(i)     
    return recipes_list_2


def search_by_time(filename: str, prep_time: int):
    new_list_2 = []
    recipes_dictionary = {}
    recipes_list_3 = []
    with open(filename) as new_file:
        for line in new_file:
            new_list_2.append(line)
        recipes_dictionary[new_list_2[0][:-1]] = int(new_list_2[1][:-1])
        counter = 0
        for i in new_list_2:
                if i == "\n":
                    recipes_dictionary[new_list_2[counter + 1][:-1]] = int(new_list_2[counter + 2][:-1])
                counter += 1
    for key, value in recipes_dictionary.items():
        if value <= prep_time:
            recipes_list_3.append(f"{key}, preparation time {value} min")
    return recipes_list_3



def search_by_ingredient(filename: str, ingredient: str):
    list_1 = []
    list_2 = [[]]
    list_3 = []
    counter_1 = 0
    with open(filename) as file:
        for line in file:
            list_1.append(line)
        for i in list_1:
            if i != "\n":
                i = i.replace("\n","")
                list_2[counter_1].append(i)
            elif i == "\n":
                list_2.append([])
                counter_1 += 1
        for i in list_2:
            for j in range(1,len(i)):
                if ingredient in i[j]:
                    list_3.append(f"{i[0]}, preparation time {i[1]} min")
                    break

    return list_3




if __name__ == "__main__": 
    found_recipes = search_by_ingredient("recipes2.txt", "fish")
    for recipe in found_recipes:
        print(recipe)








