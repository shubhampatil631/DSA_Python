def missingvalue(nums: list[int]) -> int:
    return sum(range(len(nums) + 1)) - sum(nums)

print(missingvalue([3, 2, 0, 1]))