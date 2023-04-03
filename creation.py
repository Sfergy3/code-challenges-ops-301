#!/usr/bin/env python3

# create directories
# Stanley L. Ferguson III
# 21 Mar 2023
# Create function that utilizes complete file path

# import libraries
import os 
# declare variables
filepath = input("Please enter a file path\n")
#read input
print("You entered: " + filepath)
# Declaration of functions
def giveinfo(filepath):
    for root, dirs, files in os.walk(path):
        print("Root: ", root)
        print("Sub-Directories = ", dirs)
        print("Files = ", files)
        print('-' * 10)
# Call function
giveinfo(path)
