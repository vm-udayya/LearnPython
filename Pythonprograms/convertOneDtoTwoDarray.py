import numpy as np

def convert_to_2d_array(arr, rows, cols):
    if rows * cols != len(arr):
        return "Invalid input: Number of elements in 1D array doesn't match the dimensions of the 2D array."
    
    return np.array(arr).reshape(rows, cols).tolist()

# Example usage:
arr = [1, 2, 3, 4, 5, 6]
rows = 2
cols = 3
print(convert_to_2d_array(arr, rows, cols))
