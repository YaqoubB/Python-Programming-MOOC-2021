# Write your solution here


def run(program):
    prog = {"A":0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "W":0, "X":0, "Y":0, "Z":0}
    result_list = []
    word = ""
    counter = 0
    while counter < len(program):
        line = program[counter]
        line = line.split(" ")
        if line[0] == "END":
            return result_list
        if line[0] == "PRINT":
            if line[1] in prog:
                result_list.append(prog[line[1]])
            else:
                result_list.append(int(line[1]))
        elif line[0] == "MOV":
            if line[2] in prog:
                prog[line[1]] = prog[line[2]]
            else: 
                prog[line[1]] = int(line[2])
        elif line[0] == "ADD":
            if line[2] in prog:
                prog[line[1]] += prog[line[2]]
            else:
                prog[line[1]] += int(line[2])
        elif line[0] == "SUB":
            if line[2] in prog:
                prog[line[1]] -= prog[line[2]]
            else:
                prog[line[1]] -= int(line[2])
        elif line[0] == "MUL":
            if line[2] in prog:
                prog[line[1]] *= prog[line[2]]
            else:
                prog[line[1]] *= int(line[2])
        elif line[0] == "JUMP":
            counter = program.index(line[1]+":")
        elif line[0] == "IF":
            if line[3] in prog:
                variable = prog[line[3]]
            else:
                variable = int(line[3])
            if line[2] == ">":
                if prog[line[1]] > variable:
                    if line[4] == "JUMP":
                        counter = program.index(line[5]+":")
            elif line[2] == ">=":
                if prog[line[1]] >= variable:
                    if line[4] == "JUMP":
                        counter = program.index(line[5]+":")
            elif line[2] == "<":
                if prog[line[1]] < variable:
                    if line[4] == "JUMP":
                        counter = program.index(line[5]+":")
            elif line[2] == "<=":
                if prog[line[1]] <= variable:
                    if line[4] == "JUMP":
                        counter = program.index(line[5]+":")
            elif line[2] == "==":
                if prog[line[1]] == variable:
                    if line[4] == "JUMP":
                        counter = program.index(line[5]+":")
            elif line[2] == "!=":
                if prog[line[1]] != variable:
                    if line[4] == "JUMP":
                        counter = program.index(line[5]+":")
        counter += 1
    return result_list



if __name__ == "__main__":
    program2 = ['MOV N 100', 'PRINT 2', 'MOV A 3', 'start:', 'MOV B 2', 'MOV Z 0', 'test:', 'MOV C B', 'new:', 'IF C == A JUMP virhe', 'IF C > A JUMP pass_by', 'ADD C B', 'JUMP new', 'virhe:', 'MOV Z 1', 'JUMP pass_by2', 'pass_by:', 'ADD B 1', 'IF B < A JUMP test', 'pass_by2:', 'IF Z == 1 JUMP pass_by3', 'PRINT A', 'pass_by3:', 'ADD A 1', 'IF A <= N JUMP start']
    print(run(program2))