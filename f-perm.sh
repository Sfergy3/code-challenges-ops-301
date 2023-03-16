#!/bin/bash

# file permission
# Stanley L. Ferguson III
# 15 Mar 2023
# set user permissions for file.

# prompt user for path
echo "enter path"
read path
#prompt user for file permissions
echo "enter permission"
read permission
#system sets the file permissions
chmod -R $permission $path
#look at the files
ls -al