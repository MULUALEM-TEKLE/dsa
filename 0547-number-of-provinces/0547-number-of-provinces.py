class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        grid = isConnected 
        n = len(grid)
        edges = []

        for r in range(n) : 
            for c in range(n) : 
                if r != c and grid[r][c] == 1 : edges.append([r , c])
        
        self.size = n
        par = [i for i in range(self.size)]
        
        def find(n) : 
            p = par[n]
            while p != par[p] : 
                p = par[p]
            return p 
        
        def union(n1 , n2) : 
            p1 , p2 = find(n1) , find(n2)
            if p1 != p2 : 
                par[p1] = p2
                self.size -= 1 
        
        for n1 , n2 in edges : 
            union(n1 , n2)

        return self.size 