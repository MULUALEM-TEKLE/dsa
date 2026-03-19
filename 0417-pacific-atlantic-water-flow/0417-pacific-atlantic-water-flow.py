class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights : return []
        rows , cols = len(heights) , len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(row , col , reachable_set) : 
            reachable_set.add((row , col))
            for dr , dc in [[1 , 0] , [-1 , 0] , [0 , 1] , [0 , -1]] : 
                nr , nc = row+dr , col+dc
                if (nr , nc) not in reachable_set and 0 <= nr < rows and 0 <= nc < cols : 
                    if heights[nr][nc] >= heights[row][col] : dfs(nr , nc , reachable_set)

        for i in range(rows) : 
            # pacific_initials.append((i , 0))
            dfs(i , 0 , pacific_reachable)
            # atlantic_initials.append((i , cols-1))
            dfs(i , cols-1 , atlantic_reachable)
        for i in range(cols) : 
            # pacific_initials.append((0 , i))
            dfs(0 , i , pacific_reachable)
            # atlantic_initials.append((rows-1 , i))
            dfs(rows-1 , i , atlantic_reachable)    

        return list(pacific_reachable & atlantic_reachable)
            

        

