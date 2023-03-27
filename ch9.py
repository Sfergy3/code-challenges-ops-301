#!/usr/bin/env python3

# code callennge 9
# Stanley L. Ferguson III
# 23MAR2023
# use id statements to meet conditions


# get a and b from user input
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))

# a equals b
if a == b:
    print("a is equal to b")

# a not equal to b
if a != b:
    print("a is not equal to b")

# a less than b
if a < b:
    print("a is less than b")

# a less than or equal to b
if a <= b:
    print("a is less than or equal to b")

# a greater than b
if a > b:
    print("a is greater than b")

# a greater than or equal to b
if a >= b:
    print("a is greater than or equal to b")

# create if statements with logical conditions
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")

# use elif and else to meet different conditions
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")
    if b - a >= 8:
        print("The difference between a and b is greater than or equal to 8")
    elif b - a >= 41:
        print("The difference between a and b is greater than or equal to 41")
    else:
        print("The difference between a and b is less than 8")

    # End Code
