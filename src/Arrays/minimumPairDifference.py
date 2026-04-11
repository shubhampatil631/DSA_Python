def minPairDiff(nums):
    nums.sort()
    min_diff = float('inf')
    for i in range(1,len(nums)):
        min_diff = min(min_diff,nums[i] - nums[i-1])
    result=[]
    for i in range(1,len(nums)):
        if nums[i]-nums[i-1]==min_diff:
            result.append([nums[i-1],nums[i]])
    return result
print(minPairDiff([4,2,1,3]))
        