# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root : 
            return 0
        if not root.left or not root.right : 
            return 1 + max(self.minDepth(root.left) , self.minDepth(root.right))
        else : 
            return 1 + min(self.minDepth(root.left) , self.minDepth(root.right))

        # if not root :
        #     return 0
        
        # queue = deque([[root , 1]]) 

        # while queue : 
        #     for _ in range(len(queue)) : 
        #         node , depth = queue.popleft()
        #         if not node.left and not node.right : 
        #             return depth 

        #         if node.left : 
        #             queue.append([node.left , depth + 1 ])
                
        #         if node.right : 
        #             queue.append([node.right , depth + 1 ])

