from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp=sorted(nums)
        d={}
        for i,num in enumerate(temp):
            if num not in d:
                d[num]=i
        ret=[]
        for i in nums:
            ret.append(d[i])
        return ret
s1=Solution()
print(s1.smallerNumbersThanCurrent([8,1,2,2,3]))
