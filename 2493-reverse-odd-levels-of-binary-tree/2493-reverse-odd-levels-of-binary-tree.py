# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])

        level = 0

        while q : 
            nodes , vals = [] , []
            for _ in range(len(q)) : 
                node = q.popleft()
                nodes.append(node)
                vals.append(node.val)

                if node.left : 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            if level % 2 != 0 :    
                # vals = vals[::-1]
                for i,node in enumerate(nodes) : 
                    node.val = vals[-i-1]
            
            level += 1
        
        return root
