class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        board = [['.'] * n for _ in range(n)]
        cols = set()
        posd = set()
        negd = set()

        def solve(r) : 
            if r == n : 
                self.count += 1 
                return 
            
            for c in range(n) : 
                if c in cols or r+c in posd or r-c in negd : 
                    continue 
                
                cols.add(c)
                posd.add(r+c)
                negd.add(r-c)

                solve(r+1)

                cols.remove(c)
                posd.remove(r+c)
                negd.remove(r-c)
        
        solve(0)
        return self.count