# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # temp_set = set()
        
        # cur = head
        # while cur : 
        #     temp_set.add(cur.val)
        #     cur = cur.next

        # head = ListNode()
        # cur = head
        # for i in sorted(temp_set) : 
        #     cur.next = ListNode(i)
        #     cur = cur.next

        # return head.next

        if not head or not head.next : 
            return head 
        cur = head
        while cur.next:
            if cur.val == cur.next.val : 
                cur.next = cur.next.next
            else : 
                cur = cur.next

        return head