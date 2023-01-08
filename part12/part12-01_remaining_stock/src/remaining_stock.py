# Write your solution here:

def sort_by_remaining_stock(items: list):
    def order_by_stock(item: tuple):
        return item[2]

    return sorted(items, key = order_by_stock, reverse = False) 

if __name__ == "__main__":
    sort_by_remaining_stock([("apple",1,1),("pineapple",2,2)])