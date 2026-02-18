class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        grid = isConnected 
        rows , cols = len(grid) , len(grid[0])
        self.size = len(grid)
        edges = []

        for r in range(rows) : 
            for c in range(cols) : 
                if r != c and grid[r][c] == 1 : 
                    edges.append([r , c])
        
        par = [i for i in range(self.size+1)]

        def find(n) : 
            p = par[n]
            while p != par[p] : 
                p = par[p]
            return p 
        
        def union(n1 , n2) : 
            p1 , p2 = find(n1) , find(n2)
            if p1 == p2 : 
                return 
            par[p1] = p2 
            self.size -= 1 

        for n1 , n2 in edges : 
            union(n1 , n2)
        
        return self.size

