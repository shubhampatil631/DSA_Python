def find_disappeared_numbers(nums: list[int]) -> list[int]:
    s1 = set(nums)
    ret = []
    for i in range(1, len(nums) + 1):
        if i not in s1:
            ret.append(i)
    return ret

print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))
