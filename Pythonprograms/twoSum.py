def twoSum(nums, target): # nums = [1,3,2,0]  target = 4 , output = [0,1]- indices
    final_res = {}
    for index,value in enumerate(nums): # [(0,1),(1,3),(2,2),(3,0)]
        remainder = target - value #[3,1,2,4]
        #print(final_res)
        if remainder in final_res:
            #print(final_res)
            return(final_res[remainder],index)
            
        final_res[value] = index
    return None

print(twoSum([1,3,2,0], 4))
