class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0 or k == 0 : return False 

        target = total // k 
        sub = [0] * k

        nums.sort()

        def explore(i) : 
            if i == len(nums) : 
                return True
            
            for j in range(k) : 
                if nums[i]+sub[j] <= target : 
                    sub[j] += nums[i]

                    if explore(i+1) : return True 
                
                    sub[j] -= nums[i]
            
                if sub[j] == 0 : 
                    break

            return False
        
        return explore(0)
                


        
       