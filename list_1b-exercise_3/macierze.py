#!/usr/bin/env python3

import operation_functions

def input_data(m1_rows):
    operations = {
        "+": operation_functions.add_matrix,
        "-": operation_functions.subtract_matrix,
        "*": operation_functions.multiply_matrix,
        "T": operation_functions.transpose_matrix
    }

    if m1_rows is None:
        m1_rows_input = input("Provide rows for the 1st matrix [a, b, ..., c], [a, b, ..., c]: ")
        m1_rows_input = m1_rows_input.replace("'", "")
        m1_rows = eval(m1_rows_input)

    operation_type = input("Pick an operation (+, -, *, T): ")

    m2_rows = None
    if operation_type != "T":
        m2_rows_input = input("Provide rows for the 2nd matrix [a, b, ..., c], [a, b, ..., c]: ")
        m2_rows_input = m2_rows_input.replace("'", "")
        m2_rows = eval(m2_rows_input)

    return m1_rows, m2_rows, operation_type, operations



def continue_or_stop_calculation(matrix_result):
    decision = input(f"Type 'y' to continue calculating with the result, or type 'n' to start a new calculation: ")
    if decision == "n":
        next_mat = None
        continue_calculation = True
        return continue_calculation, next_mat
    elif decision == "y":
        next_mat = matrix_result
        continue_calculation = True
        return continue_calculation, next_mat
    else:
        next_mat = None
        continue_calculation = False
        print("Closing matrix calculator")
        return continue_calculation, next_mat

def main():
    next_mat = None
    continue_calculation = True
    while continue_calculation:
        m1_rows, m2_rows, operation_type, operations = input_data(next_mat)
        calculation_function = operations[operation_type]
        if operation_type == "T":
            matrix_result = calculation_function(m1_rows)
        else:
            matrix_result = calculation_function(m1_rows, m2_rows)
        if matrix_result is not None:
            print(matrix_result)
        continue_calculation, next_mat = continue_or_stop_calculation(matrix_result)

if __name__ == "__main__":
    main()






    