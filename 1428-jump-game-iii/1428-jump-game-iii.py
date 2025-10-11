class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        nums = arr 
        n = len(nums)
        visited = [False] * n 
        @cache
        def explore(i) : 
            if visited[i] : 
                return False 
            if nums[i] == 0 : 
                return True 

            can = False
            visited[i] = True
            for j in [i-nums[i] , i+nums[i]] : 
                if 0 <= j < n : 
                    can = can or explore(j)

            return can
        
        return explore(start)