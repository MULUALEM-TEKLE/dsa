class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # n = len(nums[0])
        # nums = set(nums)

        # def explore(i , cur) : 
        #     if i == n: 
        #         return cur if cur not in nums else None
            
        #     for char in ['0' , '1'] : 
        #         res =  explore(i+1 , cur+char)
        #         if res : return res
        #     return None
        
        # return explore(0 , "")

        ans = ''
        for i , num in enumerate(nums) :
            ans += '1' if num[i] == '0' else '0'
        return ans