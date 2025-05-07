class ListNode:
    def __init__(self, val = -1) :
        self.val = val 
        self.next = None
        self.prev = None

class DoublyLinkedList : 
    def __init__(self) : 
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def push_end(self,val) : 
        new_node = ListNode(val)
        new_node.next = self.tail

        temp = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        new_node.prev = temp
    
    def top(self):
        return self.tail.prev
        

    def print_list(self):
        list_str = ""
        cur = self.head

        while cur.next != self.tail : 
            list_str += f"{cur.next.val} <-> "
            cur = cur.next

        print(list_str)
    
    def is_empty(self) : 
        return self.head.next == self.tail

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = DoublyLinkedList()
        self.history.push_end(homepage)
        self.current = self.history.top()
        

    def visit(self, url: str) -> None:
        if self.current.next != self.history.tail : 
            self.current.next = self.history.tail
            self.history.tail.prev = self.current

        self.history.push_end(url)
        self.current = self.history.top()
        self.history.print_list()
        

    def back(self, steps: int) -> str:
        step = 0
        while self.current.prev != self.history.head and step < steps:
            self.current = self.current.prev
            step += 1
        print(f"after moving{step} steps back")
        print(f"current valus is {self.current.val}")
        return self.current.val
       
        

    def forward(self, steps: int) -> str:
        step = 0
        while self.current.next != self.history.tail and step < steps:
            self.current = self.current.next
            step += 1
            
        print(f"after moving{step} steps forward")
        print(f"current valus is {self.current.val}")
        return self.current.val

       
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)