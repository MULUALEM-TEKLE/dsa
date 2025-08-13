import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Calculates the time it takes for a signal to reach all nodes in a network
        using Dijkstra's algorithm.
        
        Args:
          times: A list of edges, where times[i] = [u, v, w] represents a directed
                 edge from node u to node v with a travel time w.
          n: The number of nodes in the network.
          k: The starting node for the signal.
        
        Returns:
          The maximum time required for the signal to reach all nodes, or -1 if
          it's impossible to reach every node.
        """
        
        # Build the adjacency list for the graph.
        # Key: source node, Value: a list of (destination, weight) tuples.
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
            
        # Initialize a min-heap (priority queue) with the starting node.
        # The heap stores tuples of (time, node).
        pq = [(0, k)]
        
        # Initialize a dictionary to store the minimum time to reach each node.
        # This is more robust than a 'visited' set because it allows us to
        # update a node's time if we find a shorter path to it.
        # We start with the source node 'k' at time 0.
        dist = {node: float('inf') for node in range(1, n + 1)}
        dist[k] = 0
        
        while pq:
            # Pop the node with the minimum time from the priority queue.
            w, node = heapq.heappop(pq)
            
            # If the current time to reach this node is already greater than a
            # previously found time (stored in our dist dictionary), we have
            # found a longer, "stale" path. We can ignore it.
            if w > dist[node]:
                continue
            
            # Explore the neighbors of the current node.
            for neighbor, weight in adj[node]:
                new_time = w + weight
                
                # If we've found a shorter path to the neighbor, update its time
                # and push it to the priority queue.
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(pq, (new_time, neighbor))
                    
        # Find the maximum time from the 'dist' dictionary.
        # This will be the time for the last node to receive the signal.
        max_time = max(dist.values())
        
        # If the max time is still infinity, it means at least one node was unreachable.
        # Otherwise, return the max time.
        return max_time if max_time != float('inf') else -1

