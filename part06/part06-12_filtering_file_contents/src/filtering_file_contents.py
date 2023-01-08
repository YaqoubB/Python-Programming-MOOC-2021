# Write your solution here

def filter_solutions():
    with open("correct.csv", "w") as file:
        pass
    with open("incorrect.csv", "w") as file:
        pass
    with open("solutions.csv") as file:
        for line in file:
            line = line.replace("\n", "")
            line_1 = line.split(";")
            if "+" in line_1[1]:
                line_1[1] = line_1[1].split("+")
                if int(line_1[1][0]) + int(line_1[1][1]) == int(line_1[2]):
                    with open("correct.csv", "a") as file:
                        file.write(line+"\n")
                else:
                    with open("incorrect.csv", "a") as file:
                        file.write(line+"\n")
            if "-" in line_1[1]:
                line_1[1] = line_1[1].split("-")
                if int(line_1[1][0]) - int(line_1[1][1]) == int(line_1[2]):
                    with open("correct.csv", "a") as file:
                        file.write(line+"\n")
                else:
                    with open("incorrect.csv", "a") as file:
                        file.write(line+"\n")
    


