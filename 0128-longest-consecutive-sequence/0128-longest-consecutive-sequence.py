class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)

        for num in nums : 
            if num - 1 not in nums : 
                longest = 1 
                while num + 1 in nums : 
                    num += 1 
                    longest += 1 
                res = max(res , longest)
        return res