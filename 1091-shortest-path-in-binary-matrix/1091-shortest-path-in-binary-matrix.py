class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = cols = len(grid)
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1 : 
            return -1

        directions = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0] , [1 , 1] , [-1 , 1], [1 , -1] , [-1 , -1]]


        q = deque()
        visited = set()
        q.append((0 , 0 , 1))
        visited.add((0 , 0))

        while q : 
            row , col , level = q.popleft() 
            if row  == rows-1 and col == cols-1 : 
                return level
            
            for dr, dc in directions : 
                nr , nc = row+dr , col+dc
                if nr in range(rows) and nc in range(cols) and (nr , nc) not in visited and grid[nr][nc] == 0 : 
                    q.append((nr , nc , level+1))
                    visited.add((nr , nc))
        
        return -1
            
        
 

