#!/usr/bin/env python3

import trigonometria

def input_data():
    unit = input("Please provide the unit ('d' - degree, 'r' - radian): ")
    value = float(input("Please provide the value of the angle: "))
    calculation_type = input("Which trigonometric function do you want to calculate? ('sin', 'cos', 'tg', 'ctg'): ")

    return unit, value, calculation_type

def main():
    unit, value, calculation_type = input_data()
    if calculation_type == "sin":
        result = trigonometria.calculate_sine(value, unit)
    elif calculation_type == "cos":
        result = trigonometria.calculate_cosine(value, unit)
    elif calculation_type == "tg":
        result = trigonometria.calculate_tangent(value, unit)
    elif calculation_type == "ctg":
        result = trigonometria.calculate_cotangent(value, unit)
    else:
        print("You've probably provided wrong function.")
    print(result)

if __name__ == "__main__":
    main()