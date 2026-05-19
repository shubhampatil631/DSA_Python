nums = [2, 1, 2, 2]
ones = 0
twos = 0
for i in nums:
    ones = (ones ^ i) & ~twos
    twos = (twos ^ i) & ~ones
print(ones)