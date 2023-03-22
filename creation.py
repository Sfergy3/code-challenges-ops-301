#!/usr/bin/env python3

# create directories
# Stanley L. Ferguson III
# 21 Mar 2023
# Create function that utilizes complete file path

# import libraries
import os 

# declare variables

filepath = input("Please enter a file path\n")

# declare funtion
for (root, dirs, files) in os.walk(filepath):
  
    print("Root:", root)
    
    print("Directories: ", dirs)
  
    print("Files: ", files)

   
