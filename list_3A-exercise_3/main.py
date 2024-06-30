#!/usr/bin/env python3

#Generator that returns a list of lines with the specified string

def return_row():
    lines_with_key = []
    key = str(input("Please provide a keyword: "))
    with open('text_file.txt') as file:
        lines = file.readlines()
        for line in lines:
            if key in line:
                lines_with_key.append(line)
        return lines_with_key

line = return_row()
print(line)