class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        pq = [(grid[0][0] , 0 , 0)]
        visited = set()
        visited.add(grid[0][0])
        max_time = 0
        while pq : 
            time , row , col = heapq.heappop(pq) 
            max_time = max(time , max_time)
            if row == n-1 and col == n-1 : 
                return max_time
            
            for dr , dc in [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]] : 
                nr , nc = row+dr , col+dc
                if 0 <= nr < n and 0 <= nc < n and (nr , nc) not in visited :
                    heapq.heappush(pq , (grid[nr][nc] , nr , nc))
                    visited.add((nr , nc))
        