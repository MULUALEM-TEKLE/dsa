"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def solve(r , c , n) : 
            all_same = True 
            first_val = grid[r][c]
            for i in range(r , r+n) : 
                for j in range(c , c+n) : 
                    if grid[i][j] != first_val : 
                        all_same = False 
                        break 
                if not all_same : break
            

            if all_same : 
                return Node(first_val == 1 , True)
            
            node = Node(False , False)
            half = n // 2

            node.topLeft = solve(r , c , half)
            node.topRight = solve(r , c+half , half)
            node.bottomLeft = solve(r+half , c , half)
            node.bottomRight = solve(r+half , c+half , half)

            return node 
        
        return solve(0 , 0 , len(grid))