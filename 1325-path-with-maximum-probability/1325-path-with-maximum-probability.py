class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)

        for i in range(len(edges)) : 
            src , dst = edges[i]
            prob = succProb[i]
            adj[src].append((dst , prob ))
            adj[dst].append((src , prob ))
        
        visited = set()
        maxHeap = [(-1 , start_node)]

        while maxHeap : 
            prob1 , node1 = heapq.heappop(maxHeap)
            visited.add(node1)
            
            if node1 == end_node : 
                return prob1 * -1
            
            
            for node2,prob2 in adj[node1] : 
                if node2 not in visited : 
                    heapq.heappush(maxHeap , (prob1*prob2 , node2))

        # return highest[end_node] * -1 if end_node in highest else 0
        return 0