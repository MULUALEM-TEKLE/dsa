# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def find_min(root) : 
    cur = root
    while cur and cur.left : 
        cur = cur.left 
    return cur

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(root , key) : 
            if not root : 
                return
            
            if root.val > key : 
                root.left = delete(root.left , key)
            elif root.val < key : 
                root.right = delete(root.right , key)
            else : 
                if not root.left : 
                    return root.right 
                elif not root.right : 
                    return root.left
                else : 
                    min_val = find_min(root.right).val
                    root.val = min_val
                    root.right = delete(root.right , min_val)
            return root
        
        return delete(root , key)
            