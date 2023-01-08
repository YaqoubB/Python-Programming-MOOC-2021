# Write your solution here

def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    dictionary_1 = {}
    dictionary_1["name"] = name
    dictionary_1["director"] = director
    dictionary_1["year"] = year
    dictionary_1["runtime"] = runtime
    database.append(dictionary_1)






if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)