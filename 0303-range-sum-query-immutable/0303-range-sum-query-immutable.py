class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums 
        self.pre = []
        total = 0
        for num in nums : 
            total += num 
            self.pre.append(total)
        print(nums)
        print(self.pre)

    def sumRange(self, left: int, right: int) -> int:
        res = 0 
        if left == 0 : return self.pre[right]
        res = self.pre[right] - self.pre[left-1]
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)