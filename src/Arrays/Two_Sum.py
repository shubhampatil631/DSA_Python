def twoSum(nums,target):
    hasMap={}
    for index,val in enumerate(nums):
        diff= target - val
        if diff in hasMap:
            return [hasMap[diff],index]
        hasMap[val]=index
print(twoSum([2,11,7,15],20))