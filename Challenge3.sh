#!/bin/bash

# Script:                       Ops 301 Ops Chall #3
# Author:                       Brad Baack
# Date of latest revision:      03/27/2024
# Purpose:                      

# Prompt user for input directory path
echo "Enter the full path to the directory you want to modify:"
read directory

# Ask user for input permissions number
echo "Enter the permissions number (ex. 777, 755 etc.):"
read permissions


# Navigates to the directory input by the user and changes all files inside it to the input setting
chmod -R $permissions $directory

#Prints to the screen the directory contents and the new permissions settings of everything in the directory.
ls -al $directory