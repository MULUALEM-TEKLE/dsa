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
      
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = pre[i]-pos[i]
        
        print(res)
        return res.index(0) if 0 in res else -1