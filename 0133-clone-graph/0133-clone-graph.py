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
        if not node : return
        o2n = {}
        def clone(node) : 
            if node in o2n : return o2n[node]
            copy = Node(node.val)
            o2n[node] = copy 
            for n in node.neighbors : 
                copy.neighbors.append(clone(n))
            return copy 
        return clone(node)