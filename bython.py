#!/usr/bin/env python3

# challenge 6
# Stanley L. Ferguson III
# 23 Mar 2023
# basic bash commands in powershell.

# import the os
import os

# variables
me = [os.system("whoami")]
myip = [os.system("ip a")]
mydir = [os.system("lshw -short")]

# print variables

print (me)
print (myip)
print(mydir)
