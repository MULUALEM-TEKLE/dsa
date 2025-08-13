class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def find(i , cur) : 
            if (i , cur) in memo : return memo[(i , cur)]
            if i == len(nums) : return 1 if cur == target else 0
            
            memo[(i , cur)] = find(i+1 , cur + nums[i]) + find(i+1 , cur - nums[i])
            return memo[(i , cur)]
        
        return find(0 , 0)