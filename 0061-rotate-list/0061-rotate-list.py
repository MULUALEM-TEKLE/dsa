# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if not head or not head.next:
        #     return head

        # length = 1
        # c = head
        # while c.next:
        #     length += 1
        #     c = c.next
        # print(f"te list length is {length} ")

        # dummy = ListNode(0, head)
        # fast = dummy.next
        # counter = 1
        # effective_rotation = k % length
        # while counter <= effective_rotation:
        #     if fast.next.next == None:
        #         tmp = dummy.next
        #         dummy.next = fast.next
        #         dummy.next.next = tmp
        #         fast.next = None
        #         counter += 1
        #         fast = dummy.next
        #     else:
        #         fast = fast.next

        # return dummy.next

        if not head or not head.next or k == 0:
            return head

        fast = head
        
        length = 1
        tail = head
        while tail.next :
            tail = tail.next
            length += 1

        k = k % length
        if k == 0 : 
            return head

        for _ in range( length - k - 1 ):
            fast = fast.next
        
        new_head = fast.next
        fast.next = None
        tail.next = head
       
        return new_head

