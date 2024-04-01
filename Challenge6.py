#!/usr/bin/python3

# Script:                       Ops 301 Ops Chall #5
# Author:                       Brad Baack
# Date of latest revision:      04/1/2024
# Purpose:                      Compress log files, clear contents, and print file sizes

import os

# Declaring variables for the bash commands
whoami_command = "whoami"
ip_command = "ip a"
lshw_command = "lshw -short"

# Using the os.system() method to execute each command and print its execution status
print(f"Executing command: {whoami_command}")
os.system(whoami_command)
print("")
print("")
print(f"Executing command: {ip_command}")
os.system(ip_command)
print("")
print("")
print(f"Executing command: {lshw_command}")
os.system(lshw_command)