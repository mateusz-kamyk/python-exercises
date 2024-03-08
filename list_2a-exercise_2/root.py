#!/usr/bin/env python3

import math

def calculate_root():
    #Input value
    try:
        num = float(input("Please provide a number: "))
    except ValueError:
        print("You've provided wrong value.")
    #Root calculation
    try:
        print(math.sqrt(num))
    except ValueError:
        print("You've provided negative number.")

if __name__ == "__main__":
    calculate_root()
