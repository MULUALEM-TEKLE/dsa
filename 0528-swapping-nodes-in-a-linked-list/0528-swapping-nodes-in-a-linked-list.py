# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        array = []
        cur = head
        while cur :
            array.append(cur.val)
            cur = cur.next
        
        array[k -1], array[-k] = array[-k] , array[k -1]

        dummy = ListNode()
        cur = dummy 
        for num in array:
            cur.next = ListNode(num)
            cur = cur.next

        return dummy.next