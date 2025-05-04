class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur and i < index:
            i += 1
            cur = cur.next

        if cur:
            return cur.val

        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)

        new_node.next = self.head.next
        new_node.prev = self.head

        self.head.next.prev = new_node
        self.head.next = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)

        new_node.next = self.tail
        new_node.prev = self.tail.prev

        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head.next
        new_node = ListNode(val)
        i = 0

        while cur and i < index:
            i += 1
            cur = cur.next

        if cur  :
            new_node.next = cur
            new_node.prev = cur.prev

            cur.prev.next = new_node
            cur.prev = new_node

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        i = 0
        while cur and i < index:
            i += 1
            cur = cur.next
        if cur and cur.next and cur.prev:
            cur.next.prev = cur.prev
            cur.prev.next = cur.next

    def print_list(self):
        l = ""
        current = self.head.next
        while current != self.tail:
            l += f"{current.val} -> "
        print(l)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
