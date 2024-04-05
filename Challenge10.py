#!/usr/bin/env python3

# Script:                       Ops 301 Ops Chall #10
# Author:                       Brad Baack
# Date of latest revision:      04/5/2024
# Purpose:                      

import os

# Step 1: Create a new .txt file and append three lines
file_name = 'txtfile.txt'
with open(file_name, 'w') as file:
    file.write('First line\n')
    file.write('Second line\n')
    file.write('Third line\n')

# Step 2: Print the first line to the screen
with open(file_name, 'r') as file:
    first_line = file.readline().strip()  # Using .strip() to remove the newline character
    print(first_line)

# Step 3: Delete the .txt file
os.remove(file_name)
