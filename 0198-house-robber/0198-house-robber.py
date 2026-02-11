class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = defaultdict(int)
        def steal(i) :
            if i in cache : return cache[i] 
            if i == 0 : 
                return nums[0]
            if i == 1 : 
                return max(nums[0] , nums[1])
            
            cache[i] = max(steal(i-1) , nums[i]+steal(i-2))
            return cache[i]
        
        return steal(len(nums)-1)