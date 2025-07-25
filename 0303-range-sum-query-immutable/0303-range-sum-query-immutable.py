class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums 
        self.pre = []
        acc = 0 
        for num in nums : 
            acc += num 
            self.pre.append(acc)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0 : return self.pre[right]
        return self.pre[right] - self.pre[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)