class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        @cache
        def dp(num) : 
            if num not in nums : 
                return 0
            
            return 1+dp(num+1)
        
        ans = 0
        for num in nums : 
            ans = max(ans , dp(num))
        
        return ans