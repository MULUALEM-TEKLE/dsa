# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_gcd(n1 , n2 ) : 
            print(f"getting gcd of {n1} and {n2}")
            if n1 == n2 : 
                return n1 
            if n1 == 1  or n2 == 1 : 
                return 1
            gcd = n1 if n1 < n2 else n2 
            for i in range(gcd , 0 , -1) : 
                if n1 % i == n2 % i == 0 : 
                    return i
        
        dummy = ListNode(0)
        cur = dummy

        left = head 

        while left.next : 
            gcd = get_gcd(left.val , left.next.val)
            cur.next = ListNode(left.val)
            cur = cur.next 
            cur.next = ListNode(gcd)
            left = left.next
            cur = cur.next
        cur.next = ListNode(left.val)
        cur = dummy 
       

        return dummy.next
            