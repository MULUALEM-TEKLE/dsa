# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        flat_list = []

        cur = list1
        while cur:
            flat_list.append(cur.val)
            cur = cur.next

        cur = list2
        while cur:
            flat_list.append(cur.val)
            cur = cur.next
        
        flat_list.sort()
        if len(flat_list) == 0 : 
            return

        sorted_list = ListNode(flat_list[0])
        cur = sorted_list
        for i in range(1, len(flat_list)):
            cur.next = ListNode(flat_list[i])
            cur = cur.next

        return sorted_list

        