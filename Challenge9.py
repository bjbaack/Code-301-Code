#!/usr/bin/env python3

# Script:                       Ops 301 Ops Chall #9
# Author:                       Brad Baack
# Date of latest revision:      04/4/2024
# Purpose:                      Conditionals


# Define values for a and b
a = 5
b = 3

# Equals
if a == b:
    print("a is equal to b")

# Not Equals
if a != b:
    print("a is not equal to b")

# Less than
if a < b:
    print("a is less than b")

# Less than or equal to
if a <= b:
    print("a is less than or equal to b")

# Greater than
if a > b:
    print("a is greater than b")

# Greater than or equal to
if a >= b:
    print("a is greater than or equal to b")

# If statement with elif
if a == b:
    print("a is equal to b")
elif a > b:
    print("a is greater than b")

# If statement with both elif and else
if a == b:
    print("a is equal to b")
elif a > b:
    print("a is greater than b")
else:
    print("a is less than b")
