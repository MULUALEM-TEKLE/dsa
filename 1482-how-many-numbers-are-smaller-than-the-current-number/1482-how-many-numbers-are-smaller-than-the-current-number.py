class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        _range = range(n)
        output = [0]*n
        for i in _range:
            for j in _range:
                if nums[j] < nums[i]:
                    output[i] += 1
        return output
        