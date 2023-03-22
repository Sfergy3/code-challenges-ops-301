#!/bin/bash#

# compress logs
# Stanley L. Ferguson III
# 17 Mar 2023
# print file size to screen before filess get compressed.

# variables
backup="/var/log/backups"
syslog="/var/log/syslog"
wtmp="/var/log/wtmp"

# create a directory
mkdir -p "$backup"

# declare function for compression
process_file() {
  file="$1"
  timestamp=$(date +"%Y%m%d%H%M%S")
  zipname="$backup_dir/$(basename "$file")-$timestamp.zip"
  sizeorig=$(du -h "$file")
  zip -r "$zipname" "$file" && truncate -s 0 "$file"
  sizepost=$(du -h "$zipname")
  echo "before compression: $sizeorig, after compression: $size_after"
}

process_file "$syslog"
process_file "$wtmp"