from heapq import heappop , heappush
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)

        for i in range(len(edges)) : 
            src , dst = edges[i]
            prob = succProb[i]
            adj[src].append([dst , prob])
            adj[dst].append([src , prob])
        
        pq = [(-1.0 , start_node)]
        visited = set()
        while pq : 
            w , node = heappop(pq)
            print(f"w = {w} and node = {node}")
            if node in visited : 
                continue 
            if node == end_node : 
                return w * -1.0
            
            visited.add(node)
            
            for neighbor , prob in adj[node] : 
                if neighbor not in visited : 
                    heappush(pq , (w * prob , neighbor))
        return 0