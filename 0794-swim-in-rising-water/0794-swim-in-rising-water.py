class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visited = set()
        minh = [[grid[0][0] , 0 , 0]]
        directions = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]]
        visited.add((0 , 0))

        while minh : 
            t , r , c = heapq.heappop(minh)
            
            if r == N-1 and c == N-1 :
                return t 

            for dr , dc in directions : 
                nr , nc = r + dr , c + dc

                if nr not in range(N) or nc not in range(N) or (nr , nc) in visited: 
                    continue
                visited.add((nr , nc))  
                heapq.heappush(minh , (max(t , grid[nr][nc]) , nr , nc))
