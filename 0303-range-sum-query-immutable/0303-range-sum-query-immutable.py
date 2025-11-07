class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(nums)
        total = 0 
        self.ps = [0] * n
        for i in range(n) : 
            total += self.nums[i]
            self.ps[i] = total

    def sumRange(self, left: int, right: int) -> int:
        return self.ps[right] if left == 0 else self.ps[right] - self.ps[left-1]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)