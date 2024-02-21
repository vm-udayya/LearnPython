#Solution - additional memory
def duplicate_even_numbers(arr):
    result = []
    for num in arr:
        result.append(num)
        if num % 2 == 0:
            result.append(num)
    return result

# Example usage:
arr = [1, 2, 3, 4, 5]
print(duplicate_even_numbers(arr))  # Output: [1, 2, 2, 3, 4, 4, 5]

#Solution - No additional memory
def duplicate_even_numbers(arr):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] % 2 == 0:
            arr.insert(i, arr[i])
    return arr

# Example usage:
arr = [1, 2, 3, 4, 5]
print(duplicate_even_numbers(arr))  # Output: [1, 2, 2, 3, 4, 4, 5]


