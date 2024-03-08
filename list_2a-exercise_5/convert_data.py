#!/usr/bin/env python3

def input_data():
    try:
        data = input("Please enter data to convert: ")
        conversion_type = input("Please provide the type of conversion (to string - str, to float - fl, to integer - int): ")
    except ValueError:
        print("You've provided wrong data.")
    return data, conversion_type

def convert_data(data, conversion_type):
    try:
        if conversion_type == "str":
            converted_data = str(data)
        elif conversion_type == "fl":
            converted_data = float(data)
        elif conversion_type == "int":
            converted_data = int(data)
        else:
            print("You've entered wrong conversion type.")
    except:
        print("You've provided wrong data.")
    try:
        return converted_data
    except UnboundLocalError:
        print("Something went wrong.")

def main():
    data, conversion_type = input_data()
    converted_data = convert_data(data, conversion_type)
    print(f"Data after conversion: {converted_data}")

if __name__ == "__main__":
    main()