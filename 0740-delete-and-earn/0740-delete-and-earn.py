class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        scores = defaultdict(int)
        for num in nums : 
            scores[num] += num

        @cache
        def dfs(i) : 
            if i <= 0 : 
                return 0
            
            return max(dfs(i-1) , scores[i]+dfs(i-2))
        
        return dfs(max(nums))