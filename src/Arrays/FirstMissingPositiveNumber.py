from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s1 = set(nums)
        for i in range(1, len(nums) + 2):
            if i not in s1:
                return i

s = Solution()
print(s.firstMissingPositive([1]))