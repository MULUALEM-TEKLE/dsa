# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def find_max_node(root): 
    cur = root
    while cur.right : 
        cur = cur.right
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
                max_node = find_max_node(root.left)
                root.val = max_node.val 
                root.left = self.deleteNode(root.left , max_node.val)
        return root