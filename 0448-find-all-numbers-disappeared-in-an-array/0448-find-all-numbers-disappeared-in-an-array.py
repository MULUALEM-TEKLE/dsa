class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n) : 
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i] : 
                nums[nums[i]-1] , nums[i] = nums[i] , nums[nums[i]-1] 
        res = []
        for i in range(n) : 
            if nums[i] != i+1 : 
                res.append(i+1)
        
        return res