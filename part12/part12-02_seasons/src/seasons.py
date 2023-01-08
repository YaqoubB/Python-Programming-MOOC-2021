# Write your solution here:


def sort_by_seasons(items: list):
    def order_by_seasons(item: dict):
        return item["seasons"]

    return sorted(items, key = order_by_seasons) 

if __name__ == "__main__":
    sort_by_seasons([{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 }])