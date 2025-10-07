class UF : 
    def __init__(self , n) : 
        self.par = [i for i in range(n)]
        self.size = n
    
    def find(self , n) :
        p = self.par[n]
        while p != self.par[p] : 
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, n2 , n1) :
        print(f"n1 = {n1} and n2 = {n2}") 
        p1 , p2 = self.find(n1) , self.find(n2)
        if p1 != p2 : 
            self.par[p2] = p1
            self.size -= 1 
           
            

        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid) , len(grid[0])

        ones_count = 0 
        d = defaultdict(int)
        for r in range(rows) : 
            for c in range(cols) : 
                if grid[r][c] == "1" : 
                    d[(r , c)] = ones_count
                    ones_count += 1 
        
        uf = UF(ones_count)

        for r in range(rows) : 
            for c in range(cols) : 
                if grid[r][c] == "1" : 
                    if r > 0 and grid[r-1][c] == "1":
                        uf.union(d[(r , c)] ,d[(r-1 , c)] ) 
                    if c > 0 and grid[r][c-1] == "1" : 
                        uf.union(d[(r , c)] ,d[(r , c-1)] )

        return uf.size 