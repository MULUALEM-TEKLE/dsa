class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for i in range(len(nums)) :
            if i > 0 and nums[i] == nums[i-1] :  continue
            num = nums[i]

            low , high = i+1 , len(nums)-1

            while low < high : 
                cur_sum = num + nums[low] + nums[high]
                if cur_sum > 0 : 
                    high -= 1 
                elif cur_sum < 0 : 
                    low += 1 
                else : 
                    res.append([num , nums[low] , nums[high] ])
                    high -= 1 
                    low += 1
                    while nums[low] == nums[low-1] and low < high : 
                        low += 1
                        
        return res