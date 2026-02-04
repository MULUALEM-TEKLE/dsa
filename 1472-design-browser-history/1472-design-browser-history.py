class ListNode : 
    def __init__(self , val="" , next=None , prev=None) : 
        self.val = val
        self.next = next 
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = ListNode(homepage)
        self.head = self.history


    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        new_node.prev = self.head
        self.head.next = new_node
        self.head = new_node

    def back(self, steps: int) -> str:
        while self.head.prev and steps > 0 : 
            self.head = self.head.prev
            steps -= 1 
        return self.head.val

    def forward(self, steps: int) -> str:
        while self.head.next and steps > 0 : 
            self.head = self.head.next 
            steps -= 1 
        return self.head.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)