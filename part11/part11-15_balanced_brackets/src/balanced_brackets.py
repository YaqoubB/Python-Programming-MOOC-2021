
def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True
    my_string = "".join([ c for c in my_string if c in "([])"])

    if my_string[0] == "(" or my_string[-1] == ")":
        if my_string[0] == "(" and my_string[-1] == ")":
            return balanced_brackets(my_string[1:-1])
        else:
            return False
    if my_string[0] == "[" or my_string[-1] == "]":
        if my_string[0] == "[" and my_string[-1] == "]":
            return balanced_brackets(my_string[1:-1])
        else:
            return False


if __name__ == "__main__":
    balanced_brackets("(Hello)")