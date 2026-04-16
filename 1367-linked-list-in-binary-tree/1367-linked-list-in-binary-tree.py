# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def solve(head , node ) : 
            if not node : 
                return False 

            def walk(node , list_node ) : 
                    

                if (not node and list_node) : 
                    return False 

                if not list_node  : 
                    return True 

                if node.val == list_node.val : 
                    return walk(node.left , list_node.next) or walk(node.right , list_node.next)
                # else : 
                #     return walk(node.left , head) or walk(node.right , head)
                
            
            
            return walk(node , head) or (solve(head , node.right) or solve(head , node.left))
        
        return solve(head , root)
