#!/usr/bin/env python3

def input_1st_number():
    try:
        num1 = float(input("Please enter the 1st number: "))
    except ValueError:
        print("You've entered wrong value. You can only enter digits.")
    return num1
    
def input_operation():
    try:
        operation = input("Please enter the operation type (+, -, *, /): ")
    except ValueError:
        print("You've entered wrong value. Please enter any of the following characters: +, -, *, /.")
    return operation

def input_2nd_number():
    try:
        num2 = float(input("Please enter the 2nd number: "))
    except ValueError:
        print("You've entered wrong value. You can only enter digits.")
    return num2

def add_numbers(num1, num2):
    result = num1 + num2
    return result

def subtract_numbers(num1, num2):
    result = num1 - num2
    return result

def multiply_numbers(num1, num2):
    result = num1 * num2
    return result

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("You cannot divide by 0!")
    return result

def operation_choice(num1, operation, num2):
    if operation == "+":
        result = add_numbers(num1, num2)
    elif operation == "-":
        result = subtract_numbers(num1, num2)
    elif operation == "*":
        result = multiply_numbers(num1, num2)
    elif operation == "/":
        result = divide_numbers(num1, num2)
    else:
        print("You've provided wrong operation type.")
    return result

def main():
    num1 = input_1st_number()
    operation = input_operation()
    num2 = input_2nd_number()
    result = operation_choice(num1, operation, num2)
    print(f"The result of calculation is: {result}")

if __name__ == "__main__":
    main()
    
    

