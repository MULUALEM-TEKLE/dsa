# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        temp_arr = []
        
        while cur : 
            temp_arr.append(cur.val)
            cur = cur.next

        if len(temp_arr) == 0 : return 
        
        new_head = ListNode(temp_arr[-1])
        curr = new_head
        for i in range(2, len(temp_arr) + 1):
            new_node = ListNode(temp_arr[-i])
            curr.next = new_node
            curr = curr.next
            
        return new_head

       

        