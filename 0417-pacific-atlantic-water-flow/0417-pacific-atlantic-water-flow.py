class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights : return []
        rows , cols = len(heights) , len(heights[0])
        pacific_initials = []
        atlantic_initials = []

        for i in range(rows) : 
            pacific_initials.append((i , 0))
            atlantic_initials.append((i , cols-1))
        for i in range(cols) : 
            pacific_initials.append((0 , i))
            atlantic_initials.append((rows-1 , i))

        visited = set()
        def dfs(row , col) : 
            if not 0 <= row < rows or not 0 <= col < cols : 
                return 
            
            visited.add((row , col))
            for dr , dc in [[1 , 0] , [-1 , 0] , [0 , 1] , [0 , -1]] : 
                nr , nc = row+dr , col+dc
                if (nr , nc) not in visited and 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[row][col] : 
                    visited.add((nr ,nc))
                    dfs(nr , nc)
        # print(atlantic_initials)
        # print(pacific_initials)
        for row , col in atlantic_initials : 
            dfs(row , col)
        from_atlantic = visited 
        visited = set()
        for row , col in pacific_initials : 
            dfs(row , col)
        from_pacific = visited

        return list(from_atlantic & from_pacific)
            

        

