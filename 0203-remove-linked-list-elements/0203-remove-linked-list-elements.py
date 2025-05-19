# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # dummy = ListNode()
        # cur = dummy

        # while head : 
        #     if head.val != val : 
        #         cur.next = ListNode(head.val)
        #         cur = cur.next
        #         head = head.next
        #     else : 
        #         head = head.next 

        # return dummy.next
            
        dummy_head = ListNode(-1)
        dummy_head.next = head

        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                
        return dummy_head.next