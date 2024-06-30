#!/usr/bin/env python3

def fibonacci_seqence():
    given_n = int(input("Please provide number to which the fibonacci sequence values should be generated: "))
    a = 0
    result = 1
    while True:
        a += result
        result = a - result
        if result > given_n:
            break
        yield result

result = fibonacci_seqence()

for value in result:
    print(value)      
