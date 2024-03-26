#!/bin/bash

# Script Name:                  Append; Date and Time
# Author:                       Brad Baack
# Date of latest revision:      03/26/2024


cp /var/log/syslog "syslog_$(date '+%Y-%m-%d_%H-%M-%S')"
echo "File copied to syslog_$(date '+%Y-%m-%d_%H-%M-%S')"


# Second way
# Define the destination filename with the current date and time appended
# destination="syslog_$(date '+%Y-%m-%d_%H-%M-%S')"
# Copy /var/log/syslog to the current directory with the new filename
# cp /var/log/syslog "./${destination}"
# echo "File copied to ./${destination}"

