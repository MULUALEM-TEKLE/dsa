class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = []
        pos = [0] * len(nums)
        total = 0
        for num in nums : 
            total += num
            pre.append(total)

        total = 0
        for i in range(len(nums)-1 , -1 , -1) : 
            total += nums[i]
            pos[i] = (total)
    
   
        for i in range(len(nums)):
            if pre[i] == pos[i] : return i
        
        return -1