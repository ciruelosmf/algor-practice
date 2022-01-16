"""
Implement an integer to string conversion function,
and a string to integer conversison function,
For example, if the input to the first function is the
integer 314,it should retum the string "314" and
if the input to the second function is the string
"314" it should return the integer 314.
"""



print(314 % 10, 31 % 10, 3 % 10)
print(314//10)
print(31//10)
print(3//10)
print("")
res = ""
def intToString2(integer):
    is_negative = False
    if integer < 0:
        integer, is_negative = -integer, True
    s = []
    while True:
        s.append(chr(ord("0") + integer % 10))
        integer //= 10
        if integer == 0:
            break
    return("-" if is_negative else "") + "".join(reversed(s))


g = intToString2(314)
print(g)





