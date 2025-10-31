class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land) , len(land[0])
        directions = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]]

        res = []

        visited = set()

        def bfs(r , c ) : 
            start = [r , c]
            q = deque()
            q.append([r , c])
            visited.add((r , c))

            while q : 
                row , col = q.popleft()
                end = [row , col]
                for dr , dc in directions : 
                    nr , nc = row + dr , col + dc
                    if nr < rows and nr >= 0 and nc < cols and nc >= 0 and (nr , nc) not in visited and land[nr][nc] == 1 : 
                        q.append((nr , nc))
                        visited.add((nr , nc))
        
            res.append(start+end)

        
        for r in range(rows) : 
            for c in range(cols) : 
                if land[r][c] == 1 and (r,c) not in visited : 
                    bfs(r , c)
        
        return res
