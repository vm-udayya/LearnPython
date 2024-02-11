def containsDuplicate(nums): 
    dupSet = set(nums)
    if len(dupSet) == len(nums):
        return True
    return False

print(containsDuplicate([1,5,4,2,3]))
