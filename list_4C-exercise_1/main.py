#!/usr/bin/env python3

from datetime import datetime

def input_date():
    user_input = str(input("Please provide a date in YYYY-MM-DD HH:MM:SS, or press any key to provide current date and time: "))
    if user_input:
        try:
            time_to_convert = datetime.strptime(user_input, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("You didn't provide a specific date. Program will continue with current date.")
            user_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            time_to_convert = datetime.strptime(user_date, "%Y-%m-%d %H:%M:%S")
    else:
        user_date = datetime.now().strftime("%Y-%m-%d %H:%m:%S")
        time_to_convert = datetime.strptime(user_date, "%Y-%m-%d %H:%M:%S")
    return time_to_convert
    
def convert_to_UNIX(time_to_convert):
    unix_time = time_to_convert.timestamp()
    return unix_time

if __name__ == "__main__":
    user_date = input_date()
    unix_time = convert_to_UNIX(user_date)
    print(f"DATE: {user_date}")
    print(f"UNIX TIMESTAMP: {unix_time}")