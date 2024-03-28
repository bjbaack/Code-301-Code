#!/bin/bash

# Script:                       Ops 301 Ops Chall #4
# Author:                       Brad Baack
# Date of latest revision:      03/28/2024
# Purpose:                      Conditionals in Menu Setups

# MEnu
while true; do
    echo "Menu:"
    echo "1) Hello world"
    echo "2) Ping self"
    echo "3) IP info"
    echo "4) Exit"
    read -p "Choose an option: " choice
    
    if [ $choice = 1 ]; then
        echo "Hello World"
        echo  # This creates a space
    elif [ $choice = 2 ]; then
        ping -c 4 127.0.0.1
        echo  # This creates a space
    elif [ $choice = 3 ]; then
        ip a
        echo  # This creates a space
    elif [ $choice = 4 ]; then
        echo "Exiting..."
        exit 0
    else
        echo "Invalid option, please try again."
        echo  # This could also create a space after an invalid option message if desired
    fi
done
