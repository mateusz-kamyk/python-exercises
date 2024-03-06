import numpy as np

def add_matrix(m1_rows, m2_rows):
    matrix_result = np.add(m1_rows, m2_rows)
    return matrix_result

def subtract_matrix(m1_rows, m2_rows):
    matrix_result = np.subtract(m1_rows, m2_rows)
    return matrix_result

def multiply_matrix(m1_rows, m2_rows):
    matrix_result = np.multiply(m1_rows, m2_rows)
    return matrix_result

def transpose_matrix(m1_rows):
    matrix_result = np.transpose(m1_rows)
    return matrix_result