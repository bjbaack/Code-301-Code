#!/bin/bash

# Define the destination filename with the current date and time appended
destination="syslog_$(date '+%Y-%m-%d_%H-%M-%S')"

# Copy /var/log/syslog to the current directory with the new filename
cp /var/log/syslog "./${destination}"

echo "File copied to ./${destination}"
