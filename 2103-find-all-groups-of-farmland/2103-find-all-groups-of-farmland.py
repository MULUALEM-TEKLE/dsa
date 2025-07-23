class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows , cols = len(land) , len(land[0])
        visited = set()
        res = []

        def bfs(r , c) : 
            q = deque()
            q.append((r , c))
            visited.add((r , c))

            location = [r , c]
            end = None
            while q : 
                row , col = q.popleft()
                end = [row , col]
                directions = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]]
                for dr,dc in directions : 
                    r , c = row+dr , col+dc
                    if r in range(rows) and c in range(cols) and (r , c) not in visited and land[r][c] == 1 : 
                        q.append((r , c))
                        visited.add((r , c))
            location.extend(end)
            res.append(location)
        
        for r in range(rows): 
            for c in range(cols): 
                if land[r][c] == 1 and (r , c) not in visited : 
                    bfs(r , c)
        return res