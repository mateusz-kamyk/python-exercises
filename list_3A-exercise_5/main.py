#!/usr/bin/env python3

def prime_numbers(n):
    number = [1 for x in range(n+1)]
    for i in range(2, n+1):
        if number[i] != 0:
            yield i
            for j in range(i+i, n+1, i):
                number[j] = 0

for prime in prime_numbers(int(input("Please provide the range number: "))):
    print(prime)