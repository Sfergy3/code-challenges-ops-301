#!/bin/bash

# Append date and time
# Stanley L. Ferguson III
# 14 Mar 2023
# copy desired filepath to directory then append curent date and time.

# Copy /var/log/syslog to working directory.
cp /var/log/syslog ./
# append date and time to file
filename="syslog"
datetime=$(date +"%Y%m%d_%H%M%S")
new_filename="${filename}_${datetime}"
 cp "$filename" "$new_filename"
 # delete old file so new file can be shown with apended date and time
rm "syslog"
