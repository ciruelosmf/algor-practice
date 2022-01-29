string_to_check = "(*)*()"






def valid_parenthesis_string(stringy):
    minLeft, maxLeft = 0, 0
     

    for c in stringy:
        if c == "(":
            minLeft, maxLeft = minLeft +1 , maxLeft + 1
        elif c == ")":
            minLeft, maxLeft = minLeft - 1 , maxLeft - 1
        else:
            minLeft, maxLeft = minLeft - 1 , maxLeft + 1

    if minLeft == 0:
        return True


b = valid_parenthesis_string(string_to_check)

print(b, "valid_parenthesis_string")
