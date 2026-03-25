from typing import List

def threeSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:      # Skip duplicate elements
            continue

        low = i + 1
        high = len(nums) - 1

        while low < high:
            total = nums[i] + nums[low] + nums[high]  # type: ignore

            if total == target:
                result.append([nums[i], nums[low], nums[high]])  # type: ignore 

                while low < high and nums[low] == nums[low + 1]:   # type: ignore
                    low += 1
                while low < high and nums[high] == nums[high - 1]:  # type: ignore
                    high -= 1

                low += 1
                high -= 1

            elif total < target:
                low += 1
            else:
                high -= 1

    return result


print(threeSum([-1, 0, 1, 2, -1, -4], 0))
print(threeSum([-1, 0, 1, 2, -1, -4], 3))