#!/usr/bin/env python3

import math

def prime_number_checker(number):
    prime_number_status = True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            prime_number_status = False
    if prime_number_status == True:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is NOT a prime number")

number = int(input("Enter a number to check if it's a prime number: "))
prime_number_checker(number)