class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_len = sum(matchsticks)
        if total_len % 4 != 0 : 
            return False
        side_len = total_len // 4 
        sides = [0]*4
        matchsticks.sort(reverse=True)

        def dfs(i) : 
            if i == len(matchsticks) : 
                return True
            for side in range(4) : 
                if sides[side] + matchsticks[i] <= side_len : 
                    sides[side] += matchsticks[i]
                    if dfs(i+1) : 
                        return True 
                    sides[side] -= matchsticks[i]
            return False
        return dfs(0)