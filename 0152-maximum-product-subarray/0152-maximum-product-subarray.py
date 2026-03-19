class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = 1
        cur_max = 1
        res = nums[0]

        for num in nums : 
            if num == 0 : 
                cur_min , cur_max = 1 , 1
                res = max(res , 0)
                continue 

            old_max = cur_max

            cur_max = max(num , num*cur_max , num*cur_min)

            cur_min = min(num , num*old_max , num*cur_min)

            res = max(res , cur_min , cur_max)
        
        return res