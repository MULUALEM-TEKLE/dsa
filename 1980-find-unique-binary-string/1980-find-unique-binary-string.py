class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums = set(nums)
        chars = ['0' , '1']

        def explore(i , cur) : 
            # print(cur)
            if i == n: 
                if cur not in nums : 
                    # print(f'{cur} not in nums')
                    return cur
                return
            res = None
            for char in chars : 
                res =  explore(i+1 , cur+char)
                if res : return res
            return res 
        
        return explore(0 , "")