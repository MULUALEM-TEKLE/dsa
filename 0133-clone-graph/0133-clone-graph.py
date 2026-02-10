"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node : 
            return None

        start = node 
        o_to_n = {}
        
        def dfs(node) : 
            o_to_n[node] = Node(node.val)
            for nei in node.neighbors :
                if nei not in o_to_n : 
                    dfs(nei)
        
        dfs(start)
        
        for o , n in o_to_n.items() :
            for nei in o.neighbors : 
                n.neighbors.append(o_to_n[nei]) 
        
        return o_to_n[start]
