def missingNumber(nums):
    asc_num = sorted(nums)
    for i in range(len(asc_num)):
        if i != asc_num[i]:
            return i
    return len(asc_num)

print(missingNumber([1, 0, 3, 2, 5]))  # Output: 4
