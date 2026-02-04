class ListNode :
    def __init__(self, val=0 , next=None)  : 
        self.val = val 
        self.next = next

def print_list(head) : 
    s = ""
    while head : 
        s += f"{head.val}->"
        head = head.next 
    print(s[:-2])

class MyLinkedList:

    def __init__(self):
        self.head = ListNode() 

    def get(self, index: int) -> int:
        cnt = -1
        cur = self.head
        while cur : 
            if cnt == index : 
                return cur.val
            cnt += 1 
            cur = cur.next 
        
        return -1 

    def addAtHead(self, val: int) -> None:
        cur = self.head.next
        new_node = ListNode(val)
        new_node.next = cur 
        self.head.next = new_node
        # print_list(self.head)

    def addAtTail(self, val: int) -> None:
        cur = self.head
        while cur.next : 
            cur = cur.next 

        new_node = ListNode(val)
        cur.next = new_node 
        # print_list(self.head)

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head
        cnt = -1
        while cur : 
            if cnt + 1 == index : 
                bef = cur 
                nxt = cur.next 
                new_node = ListNode(val)
                bef.next = new_node
                new_node.next = nxt
            cur = cur.next
            cnt += 1 
        # print_list(self.head)

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head 
        cnt = -1
        while cur and cur.next : 
            if cnt + 1 == index : 
                cur.next = cur.next.next
            cur = cur.next 
            cnt += 1 
        # print_list(self.head)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)