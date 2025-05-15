# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # array = []
        # cur = head
        # while cur :
        #     array.append(cur.val)
        #     cur = cur.next
        
        # array[k -1], array[-k] = array[-k] , array[k -1]

        # dummy = ListNode()
        # cur = dummy 
        # for num in array:
        #     cur.next = ListNode(num)
        #     cur = cur.next

        # return dummy.next

        cur = head 
        for i in range(k-1) : 
            cur = cur.next
        
        # print(f"cur is at {cur.val}")

        right = head 
        left = cur 

        while cur.next : 
            cur = cur.next 
            right = right.next 

        right.val , left.val = left.val, right.val
        return head
        # print(f"finally left ia at {left.val} and right is at {right.val}")