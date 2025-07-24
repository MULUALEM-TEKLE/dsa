class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)

        for num in nums : 
            if num-1 not in nums : 
                nxt = num + 1 
                cur = 1 
                while nxt in nums : 
                    nxt += 1 
                    cur += 1 
                longest = max(longest , cur)
        return longest