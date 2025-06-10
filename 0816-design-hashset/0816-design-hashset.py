class MyHashSet:

    def __init__(self):
        self.size = 0
        self.capacity = 10
        self.buckets = [[] for _ in range(self.capacity)]
    
    def hash(self, key) : 
        return key % self.capacity
    
    def rehash(self) : 
        self.capacity = 2 * self.capacity 
        new_buckets = [[] for _ in range(self.capacity)]

        old_buckets = self.buckets 
        self.buckets = new_buckets
        self.size = 0 

        for chain in old_buckets : 
            for item in chain : 
                self.add(item)

    def add(self, key: int) -> None:
        index = self.hash(key)
        chain = self.buckets[index]
        if key not in chain : 
            chain.append(key)
            self.size += 1

        if self.size >= self.capacity // 2 : self.rehash()
                

    def remove(self, key: int) -> None:
        index = self.hash(key)
        chain = self.buckets[index]

        for index , item in enumerate(chain) : 
            if item == key : del chain[index]

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        chain = self.buckets[index]

        # print(self.buckets)

        for item in chain : 
            if item == key : return True
        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)