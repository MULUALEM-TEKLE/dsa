class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights) , len(heights[0])
        directions = [[0 , 1] , [0 , -1] , [1 , 0], [-1 , 0]]

        pq  = [(0 , 0 , 0)]
        visited = set()

        while pq : 
            diff , r , c = heapq.heappop(pq)

            if (r , c) in visited : continue

            if r == rows-1 and c == cols -1 : 
                return diff 

            visited.add((r , c))
            for dr , dc in directions : 
                nr , nc = r+dr , c+dc 
            
                if nr not in range(rows) or nc not in range(cols) or (nr , nc) in visited : 
                    continue 
                new_diff = abs(heights[r][c] - heights[nr][nc])
                new_diff = max(new_diff , diff)
                heapq.heappush(pq , (new_diff , nr , nc))
