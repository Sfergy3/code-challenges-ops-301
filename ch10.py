#!/usr/bin/env python3

# Chall 10
# Stanley L. Ferguson III
# 24 Mar 2023
# create a a file to read and write in then remove the file


# Opens a new file named in test.txt in write mode and appends three lines
with open("test.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

# Opens the file in read mode and prints the first 3 lines
with open("test.txt", "r") as file:
    for i in range(3):
        lines = file.readline()
        print(lines)

# Deletes the file
import os
os.system("rm test.txt")
