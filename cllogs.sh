#!/bin/bash#

# compress logs
# Stanley L. Ferguson III
# 17 Mar 2023
# print file size to screen before filess get compressed.

# get file sizes
stat /var/log/syslog
stat var/log/wtmp 

#prompt for compression
echo "would you like to compress the files (y/n)"
read input
if [[ input == y ]]; then
    $ zip /var/log/syslog.zip /var/log/syslog
