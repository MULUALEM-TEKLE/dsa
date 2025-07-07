# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         def steal(n) :
#             if n == 0 : 
#                 return nums[0]
#             if n == 1 : 
#                 return max(nums[0] , nums[1])
#             return max(nums[n]+steal(n-2) , steal(n-1))
#         return steal(len(nums)-1)

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 1 : return nums[0]
#         memo = {0 : nums[0] , 1 : max(nums[0] , nums[1])}
#         def steal(n) :
#             if n in memo : 
#                 return memo[n]
#             memo[n] = max(nums[n]+steal(n-2) , steal(n-1))
#             return memo[n]
#         return steal(len(nums)-1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 : 
            return nums[0]
        if n == 2 : 
            return max(nums[0] , nums[1])
        
        dp = [nums[0] , max(nums[0] , nums[1])]
        for i in range(2 , n) :
            dp[0] , dp[1] = dp[1] , max(dp[0] + nums[i] , dp[1] ) 
        return dp[1]
            