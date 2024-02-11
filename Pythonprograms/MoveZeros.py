def moveZeros(nums): # nums = [0]
    counter = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            counter +=1
            print(counter)
        else:
            if counter > 0:
                nums[i - counter] = nums[i] 
                nums[i] = 0
    return nums
    

print(moveZeros([0,0,1,0,2,3,4,]))
            
