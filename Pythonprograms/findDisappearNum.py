def findDisappearedNumbers(nums):
    num_set = set(nums) # Create a set of unique numbers in the array
    print(num_set)
    n = len(nums)
    disappeared = []

    # Iterate from 1 to n, check if each number exists in the set
    for i in range(1, n + 1):
        if i not in num_set:
            disappeared.append(i)

    return disappeared

# Example usage:
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(nums))  # Output: [5, 6]
