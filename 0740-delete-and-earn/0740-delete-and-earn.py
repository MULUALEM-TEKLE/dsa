class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        scores = defaultdict(int)

        for num in nums : 
            scores[num] += num
        
        u_nums = sorted(scores.keys())
        
        @cache
        def explore(i) : 
            if i < 0 : 
                return 0
            if i == 0 : 
                return scores[u_nums[0]]
            
            skip = explore(i-1)

            if u_nums[i] == u_nums[i-1] + 1 : 
                take = scores[u_nums[i]] + explore(i-2)
            else : 
                take = scores[u_nums[i]] + explore(i-1)
            
            return max(take , skip)
        
        return explore(len(u_nums)-1)