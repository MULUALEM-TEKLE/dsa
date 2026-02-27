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

        o2n = { }

        def build(root) : 
          
            o2n[root] = Node(root.val)

            for neighbor in root.neighbors : 
                if neighbor not in o2n : 
                   build(neighbor)
        
        # def copy(root) : 
        #     if not root : 
        #         return 

        #     if root in o2n : 
        #         return o2n[root]
            
        #     cp = Node(root.val)
        #     o2n[root] = cp

        #     for neighbor in root.neighbors : 
        #         cp.neighbors.append(copy(neighbor))
            
        #     return cp 
        
        build(node)

        for old , n in o2n.items() : 
            for neighbor in old.neighbors : 
                n.neighbors.append(o2n[neighbor])


        return o2n[node]