#!/usr/bin/env python3

def input_and_open_file():
    try:
        file_name = input("Enter file name: ")
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found. Try again.")
        file_name = input("Enter file name again: ")
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)

input_and_open_file()
