# Write your solution here:

class Series:
    def __init__(self, title: str, seasons: int, genre: list):
        self.title = title
        self.seasons = seasons
        self.genre = genre
        self.reviews = []
        self.average = 0


    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.reviews.append(rating)
        quantity = len(self.reviews)
        total = sum(self.reviews)
        average = total / quantity
        self.average = average
  
    def highest_rating(self):        #helper function
        s_list = sorted(self.reviews)
        return s_list[-1]      

            
    def __str__(self):
        genre_list = self.genre
        genre_string = ", ".join(genre_list)
        ratings_string = ""
        if len(self.reviews) > 0:
            ratings_string = f"{len(self.reviews)} ratings, average {self.average:.1f} points"
        else:
            ratings_string = "no ratings"
        return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\n{ratings_string}"
        
def minimum_grade(rating: float, series_list: list):
    list_1 = []
    for i in series_list:
        highest = i.highest_rating()
        if highest >= rating:
            list_1.append(i)
    return list_1


def includes_genre(genre: str, series_list: list):
    list_2 = []
    for i in series_list:
        g_exist = i.genre
        if genre in g_exist:
            list_2.append(i)
    return list_2


if __name__ == "__main__":

    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    dexter.rate(4)
    dexter.rate(5)
    dexter.rate(5)
    dexter.rate(3)
    dexter.rate(0)
    print(dexter)

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)