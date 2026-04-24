class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solution = []

        board = [['.'] * n for _ in range(n)]

        cols = set()
        posd = set()
        negd = set()


        def solve(r) : 
            if r == n : 
                solution.append(["".join(r) for r in board])
                return 
            
            for c in range(n) : 
                if c in cols or (r+c) in posd or (r-c) in negd : 
                    continue 
                
                board[r][c] = "Q"
                cols.add(c)
                posd.add(r+c)
                negd.add(r-c)

                solve(r+1)

                board[r][c] = "."
                cols.remove(c)
                posd.remove(r+c)
                negd.remove(r-c)
        
        solve(0)
        return solution

                
