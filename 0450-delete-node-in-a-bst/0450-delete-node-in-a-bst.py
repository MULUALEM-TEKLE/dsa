# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def find_min(root) : 
    cur = root 
    while cur.left : 
        cur = cur.left
    return cur
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root : 
            return None
        
        if key > root.val : 
            root.right = self.deleteNode(root.right , key)
        elif key < root.val : 
            root.left = self.deleteNode(root.left , key)
        else : 
            if not root.left : 
                return root.right 
            elif not root.right : 
                return root.left
            else : 
                min_node = find_min(root.right)
                root.val = min_node.val 
                root.right = self.deleteNode(root.right , root.val)
        return root
