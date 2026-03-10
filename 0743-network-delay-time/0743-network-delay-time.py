class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for src , dst , time in times : 
            adj[src].append([dst , time])
        
        min_times = {}
        pq = [(0 , k)]
        while pq : 
            time , node = heapq.heappop(pq)
            if node in min_times : 
                continue
            min_times[node] = (time)
            for nei , nei_time in adj[node] : 
                if nei not in min_times :
                    heapq.heappush(pq , (time+nei_time , nei))
        
        if len(min_times) == n : return max(min_times.values())
        return -1