# Write your solution here

def filter_incorrect():
    with open("lottery_numbers.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line_1 = line.split(";")
            try:
                if "week " not in line_1[0][0:4] or int(line_1[0][4:]) < 1 or int(line_1[0][4:]) > 39:
                    raise ValueError
                line_1[1] = line_1[1].split(",")
                if len[line_1[1]] != 7:
                    raise ValueError
                for i in line_1[1]:
                    i = int(i)
                    if i < 1 or 1 > 39:
                        raise ValueError
                for i in line_1[1].sort():
                    if i in line_1[1]:
                        line_1[1].pop(i)
                        if i in line[1]:
                            raise ValueError
                with open("correct_numbers.csv", "w") as file:
                    file.write(line+"\n")

            except ValueError:
                pass

                