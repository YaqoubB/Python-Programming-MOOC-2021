# Write your solution here

import json

class Player:
    def __init__(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self.__name = name
        self.__nationality = nationality
        self.__assists = assists
        self.__goals = goals
        self.__penalties = penalties
        self.__team = team
        self.__games = games

    def name(self):
        return self.__name
    
    def nationality(self):
        return self.__nationality
    
    def assists(self):
        return self.__assists

    def goals(self):
        return self.__goals

    def penalties(self):
        return self.__penalties

    def team(self):
        return self.__team

    def games(self):
        return self.__games

    def player_points(self):
        return self.__goals + self.__assists
    
    def highest_points(self):
        return (self.__goals + self.__assists)  * 100 + self.__goals
    
    def highest_goals(self):
        return (self.__goals * 100) - self.__games  
    

    def __str__(self):
        return f"{self.__name:20} {self.__team} {self.__goals:>3} + {self.__assists:>2} = {self.player_points():>3}"
  

class PlayerBook:
    def __init__(self):
        self.__player_list = {}

    def add_player(self, player: dict):
        self.__player_list[player["name"]] = Player(player["name"], player["nationality"], player["assists"], player["goals"], player["penalties"], player["team"], player["games"])

    def len(self):
        return len(self.__player_list)

    def get_player(self, name: str):
        if name not in self.__player_list:
            return None
        return self.__player_list[name]
    
    def get_teams(self):
        return sorted(set([value.team() for key, value in self.__player_list.items()]))

    def get_countries(self):
        return sorted(set([value.nationality() for key, value in self.__player_list.items()]))

    def get_team_players(self, team):
        return sorted([value for key, value in self.__player_list.items() if value.team() == team], key = lambda x : x.player_points(), reverse = True)
    
    def get_country_players(self, country):
        return sorted([value for key, value in self.__player_list.items() if value.nationality() == country], key = lambda x : x.player_points(), reverse = True)

    def get_highest_players(self, quantity):
        return sorted([value for key, value in self.__player_list.items()], key = lambda x : x.highest_points(), reverse = True)[:quantity]

    def get_highest_goals(self, quantity):
        return sorted([value for key, value in self.__player_list.items()], key = lambda x : x.highest_goals(), reverse = True)[:quantity]

    def __str__(self):
        pass



class FileHandler():
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self):
        with open(self.__filename) as my_file:
            data = my_file.read()
        file_of_dict = json.loads(data)
        return file_of_dict


class PlayerBookApplication:
    def __init__(self, storage_service):
        self.__playerbook = PlayerBook()
        self.__file_of_dict = storage_service

        for dict in self.__file_of_dict:
            self.__playerbook.add_player(dict)

    def get_name(self):
        name = input("name: ")
        player = self.__playerbook.get_player(name)
        if player == None:
            print("no entry for this course")
        else:
            print(player)

    def get_teams(self):
        [print(i) for i in self.__playerbook.get_teams()]

    def get_countries(self):
        [print(i) for i in self.__playerbook.get_countries()]
    
    def get_team_player_points(self):
        team = input("team: ")
        [print(i) for i in self.__playerbook.get_team_players(team)]
    
    def get_country_player_points(self):
        country = input("country: ")
        [print(i) for i in self.__playerbook.get_country_players(country)]

    def get_players_most_points(self):
        quantity = int(input("how many: "))
        [print(i) for i in self.__playerbook.get_highest_players(quantity)]

    def get_players_most_goals(self):
        quantity = int(input("how many: "))
        [print(i) for i in self.__playerbook.get_highest_goals(quantity)]

    def help(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")


    def execute(self):
        print(f"read the data of {self.__playerbook.len()} players")
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.get_name()
            elif command == "2":
                self.get_teams()
            elif command == "3":
                self.get_countries()  
            elif command == "4":
                self.get_team_player_points() 
            elif command == "5":
                self.get_country_player_points() 
            elif command == "6":
                self.get_players_most_points() 
            elif command == "7":
                self.get_players_most_goals() 
            else:
                self.help()

 

filename = input("file name: ")
storage_service = FileHandler(filename).load_file()
application = PlayerBookApplication(storage_service)
application.execute()



