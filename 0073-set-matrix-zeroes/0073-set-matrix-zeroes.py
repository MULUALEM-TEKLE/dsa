class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows , cols = len(matrix) , len(matrix[0])
        # visited = set()
        def mark(r , c) : 
            # visited.add((r , c))
            for i in range(rows) : 
                matrix[i][c] = 0
                # visited.add((i , c))
            
            for i in range(cols) : 
                matrix[r][i] = 0
                # visited.add((r , i))
        locations = deque()
        for r in range(rows) : 
            for c in range(cols) : 
                if matrix[r][c] == 0  : 
                    locations.append((r , c))
        while locations : 
            r , c = locations.popleft()
            mark(r , c)