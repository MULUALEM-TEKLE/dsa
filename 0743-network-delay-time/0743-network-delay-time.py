class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for src , dst , time in times : 
            adj[src].append([dst , time])
        
        min_times = []
        pq = [(0 , k)]
        visited = set()
        visited.add(k)
        while pq : 
            time , node = heapq.heappop(pq)
            if node in visited : 
                continue
            visited.add(node)
            min_times.append(time)
            for nei , nei_time in adj[node] : 
                if nei not in visited :
                    heapq.heappush(pq , (time+nei_time , nei))
        
        if len(min_times) == n : return max(min_times)
        return -1