class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        N = max(nums) + 2 

        bucket = [0] * N 

        for num in nums : 
            bucket[num+1] += 1 
        
        print(bucket)
        
        for i in range(1 , N) : 
            bucket[i] += bucket[i-1]
        
        print(bucket)
        
        return [bucket[num] for num in nums]