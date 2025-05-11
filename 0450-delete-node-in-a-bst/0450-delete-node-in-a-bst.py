# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def min_val_node(root) :
    cur = root
    while cur and cur.left:
        cur = cur.left
    return cur
 
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # base condition, reached the end of the leaves
        if not root :
            return None
        # if val is greater than the current root
        if key > root.val : 
            root.right = self.deleteNode(root.right , key)
            # recursively find and remove the node containing val from the right subtree
            # and return the value to the current root right
        # else if val is less than the current root
        elif key < root.val :
            root.left = self.deleteNode(root.left , key)
            # recursively find and remove the node containing val from the left subtree
            # and return the value to the current root left

        # else if val is equal to current node's value:
        else : 
        
            # now we've got a match
            # check if the node has a child on either side or on both sides
            # if node has a child on the right side
            if not root.left:
                return root.right
                # return the left child back
            #if the node has child on the left side
            elif not root.right :
                return root.left
                # return the right side back
            # if the node has both left and right child
            else:
                # find the minimum value from the right subtree or the max value from the left subtree
                min_node = min_val_node(root.right)
                # (this will ensure our tree will stay relatively balanced and correct) 
                # then set the root.val to that minimum node.val
                root.val = min_node.val
                # then recursively find and remove that minimum node from the right or maximum node from the left
                # and assign it back to the right/left of the new root node's right/left side
                root.right = self.deleteNode(root.right, min_node.val)
        # return node
        return root


        