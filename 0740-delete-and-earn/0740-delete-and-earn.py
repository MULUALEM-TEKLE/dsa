class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        scores = defaultdict(int)

        for num in nums : 
            scores[num] += num
        
        @cache
        def explore(i) : 
            if i <= 0 : 
                return 0
            return max(scores[i] + explore(i-2) , explore(i-1))
        
        return explore(max(nums))