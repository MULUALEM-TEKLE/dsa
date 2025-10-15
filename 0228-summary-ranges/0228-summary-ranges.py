class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []

        i = 0 

        while i < len(nums) : 
            start = i
            while i < len(nums)-1 and nums[i] + 1 == nums[i+1] : 
                i += 1
            if start != i : 
                res.append(f"{nums[start]}->{nums[i]}") 
            else : 
                res.append(f"{nums[start]}")
            i += 1 
        
        return res 