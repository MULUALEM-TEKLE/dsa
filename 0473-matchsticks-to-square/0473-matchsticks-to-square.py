class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matches = matchsticks
        total_len = sum(matches)
        if total_len % 4 != 0 : return False 
        side_length = total_len/4
        matches.sort(reverse=True)
        sides = [0] * 4
        # @cache
        def dfs(i) : 
            if i == len(matches) : return True 
            for side in range(4) : 
                if sides[side] + matches[i] <= side_length : 
                    sides[side] += matches[i] 
                    if dfs(i+1) : return True 
                    sides[side] -= matches[i]
            return False
        return dfs(0)
