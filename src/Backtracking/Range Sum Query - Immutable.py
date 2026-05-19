class NumArray:

    def __init__(self, nums: List[int]):
        self.acc_num=[0]
        for num in nums:
            self.acc_num.append(self.acc_num[-1]+num)
    def sumRange(self, left: int, right: int) -> int:
        return self.acc_num[right+1] - self.acc_num[left]
