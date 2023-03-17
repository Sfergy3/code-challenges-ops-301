#!/bin/bash

#conditions
#Stanley L. Ferguson III
#16 mar 2023
#give user a prompt of options

while true; do

    echo "what would you like to do today? enter:
    1) print hello world
    2) ping self
    3) ip info
    4) exit"
    read input

    if [[ $input -eq 1 ]]; then
        echo "hello world"
    elif [[ $input -eq 2 ]]; then
        echo "hit Ctl C to stop"
        ping 192.168.1.204
    elif [[ $input -eq 3 ]]; then
        ip a 
    elif [[ $input -eq 4 ]]; then
        break
    else
        echo "invalid input"
    fi
done