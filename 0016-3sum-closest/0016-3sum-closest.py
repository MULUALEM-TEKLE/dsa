class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
       
        n = len(nums)
        nums.sort()
        closest_sum = float("inf")

        for i,num in enumerate(nums) : 
            # if i > 0 and i < n-1 and nums[i] == nums[i+1] : continue
            left , right = i + 1 , n - 1

            while left < right : 
                cur_sum = num + nums[right] + nums[left] 
                
                if abs(cur_sum-target) < abs(closest_sum-target) : 
                    closest_sum = cur_sum
                
                if cur_sum == target : 
                    return cur_sum
                elif cur_sum < target : 
                    left += 1
                else : 
                    right -= 1 

        return closest_sum 