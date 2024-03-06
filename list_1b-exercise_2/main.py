#!/usr/bin/env python3

import czas

def input_data():
    provided_unit = input("Provide a time unit (s - seconds, m - minutes, h - hours): ")
    value = float(input("Provide the amount of time in the previously selected unit: "))
    return provided_unit, value

def converter(provided_unit, value):
    if provided_unit == "s":
        result = czas.sec_to_min(value)
        end_value = "minutes"
    elif provided_unit == "m":
        result = czas.min_to_hour(value)
        end_value = "hours"
    elif provided_unit == "h":
        result = czas.hours_to_days(value)
        end_value = "days"
    else:
        print("This calculator doesn't support this operation.")
        return
    
    print(result, end_value)

def main():
    provided_unit, value = input_data()
    converter(provided_unit, value)

if __name__ == "__main__":
    main()