def containDuplicate2(nums,k):
    seen=set()
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        seen.add(nums[i])
        if i>=k:
            seen.remove(nums[i-k])
    return False
print(containDuplicate2([1,2,3,1],3))