class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        directions = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]]
        # have a set of lands on the edges 
        edge_lands = []
        center_lands = []
        patches_count = 0
        center_counts = 0 
        for r in range(rows) : 
            for c in range(cols) : 
                if (r == 0 or r == rows-1) and grid[r][c] == 1 : 
                    edge_lands.append((r,c))
                    patches_count += 1
                elif (c == 0 or c == cols-1) and grid[r][c] == 1 : 
                    edge_lands.append((r , c))
                    patches_count += 1 
                elif grid[r][c] == 1 :
                    center_lands.append((r , c)) 
                    patches_count += 1
                    center_counts += 1 

        def explore(r , c  , visited) : 
            if r not in range(rows) or c not in range(cols) or (r , c) in visited or grid[r][c] == 0 : 
                return 
            grid[r][c] = 0 
            visited.add((r , c))
            for dr , dc in directions : 
                nr , nc = r+dr , c+dc 
                explore(nr , nc , visited)
            
        for r , c in edge_lands : 
            explore(r , c, set())

        res = 0
        for r in range(rows) :
            for c in range(cols) : 
                if grid[r][c] == 1 : 
                    res += 1 

        return res 

