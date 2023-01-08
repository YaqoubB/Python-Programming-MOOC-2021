# Write your solution here

def new_person(name: str, age: int):
    if  "*" in name:
        raise ValueError
    if name == "":
        raise ValueError
    if " " not in name:
        raise ValueError
    if len(name) > 40:
        raise ValueError
    if age < 0:
        raise ValueError
    if age > 150:
        raise ValueError
    try:
        return (name , age)
    except ValueError:
        pass
        
if __name__ == "__main__":
    print(new_person('Andrew', 32))