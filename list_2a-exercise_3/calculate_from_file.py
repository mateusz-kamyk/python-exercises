#!/usr/bin/env

def input_file():
    data = input("Please provide file path: ")
    return data

def open_file(data):
    added = 0
    try:
        with open(data, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    added += number
                except ValueError:
                    print("Error: File has to contain only numbers.")
    except FileNotFoundError:
        print("File not found.")
    print(f"Sum of the provided data: {added}")

data = input_file()
open_file(data)