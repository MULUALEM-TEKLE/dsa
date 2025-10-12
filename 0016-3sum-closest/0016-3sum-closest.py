class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res_up = float('inf')
        res_down = float('-inf')
        n = len(nums)
        nums.sort()

        for i,num in enumerate(nums) : 
            # print(f"checking for {i} index num {num}")
            left , right = i + 1 , n - 1
            # print(f"now left is {left} and right is {right}")
            while left < right : 
                if num + nums[right] + nums[left] > target : 
                    res_up = min(res_up , num + nums[right] + nums[left])
                    right -= 1 
                elif num + nums[right] + nums[left] < target : 
                    res_down = max(res_down , num + nums[right] + nums[left])              
                    # print(f"maximum res_down found so far {res_down}")
                    left += 1 
                else : 
                    return num + nums[right] + nums[left]

        if abs(target - res_up) < abs(target-res_down) : 
            return res_up 
        return res_down 