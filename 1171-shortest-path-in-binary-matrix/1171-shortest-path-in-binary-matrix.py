class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])

        if grid[0][0] != 0 or grid[rows-1][cols-1] !=0 : 
            return -1
        
        if rows == 1 and cols == 1: return 1 

        visited = set()
        q = deque()
        visited.add((0 , 0))
        q.append((0 , 0 , 1))
        

        while q : 
            row , col, length = q.popleft()

            if row == rows-1 and col == cols-1 : 
                return length  

            directions = [[0 , 1] ,[0 ,-1] , [1 , 0] , [-1 , 0] , [1 , 1] , [-1 , 1] , [1 , -1] , [-1 , -1]]

            for dr , dc in directions : 
                r , c = row + dr , col + dc

                if r in range(rows) and c in range(cols) and (r , c) not in visited and grid[r][c] == 0 : 
                    q.append((r , c , length+1))
                    visited.add((r, c))
        return -1
    
    


                    
