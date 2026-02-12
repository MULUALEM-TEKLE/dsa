class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # lets find the max in the array, not assuming its circular
        global_max , cur_max = nums[0] , 0
        total = 0 
        for num in nums : 
            total += num
            cur_max = max(num , cur_max+num)
            global_max = max(global_max , cur_max)
        print(global_max)

        # lets find the min_sum inside of the array, once we subtract this from the total we can find the max circular sum =)
        global_min , cur_min = nums[0] , 0
        for num in nums : 
            cur_min = min(num , cur_min+num)
            global_min = min(global_min , cur_min)

        print(global_min)
        print(total)
        return max(global_max , total-global_min) if global_max > 0 else global_max