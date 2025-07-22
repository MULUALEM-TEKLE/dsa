# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

            
        # s = ''
        # while prev : 
        #     s += f'{prev.val}->'
        #     prev = prev.next 
        # print(s[:-2])

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
       

        fast = slow = head 
        while fast and fast.next : 
            slow = slow.next
            fast = fast.next.next 

        prev = None
        cur = slow         

        while cur : 
            nxt = cur.next 
            cur.next = prev 
            prev = cur 
            cur = nxt 

        res = float('-inf')
        while prev :
            res = max(res , head.val + prev.val)
            head = head.next
            prev = prev.next 
        
        return res

