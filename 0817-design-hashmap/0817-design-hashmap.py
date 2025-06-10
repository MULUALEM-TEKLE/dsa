class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MyHashMap:

    def __init__(self):
        self.size = 0
        self.capacity = 10 # Starting with a small capacity for demonstration
        self.load_factor_threshold = 0.5 # Rehash when size / capacity >= 0.5
        self.buckets = [[] for _ in range(self.capacity)] # Renamed from 'map'
    
    def hash(self, key) : 
        return key % self.capacity
    
    def rehash(self) : 
        # print(f"Rehashing from capacity {self.capacity} to {2 * self.capacity}")
        self.capacity *= 2 # Double the capacity
        new_buckets = [[] for _ in range(self.capacity)] # New bucket array
       
        old_buckets = self.buckets # Keep a reference to the old buckets
        self.buckets = new_buckets # Update self.buckets to the new array
        self.size = 0 # Reset size, will be re-counted by put operations

        # Re-insert all existing key-value pairs into the new, larger map
        for chain in old_buckets:
            for pair in chain:
                # Use the existing put method to correctly re-hash and insert
                self.put(pair.key, pair.value) 

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        chain = self.buckets[index]

        # Iterate through the chain to find if the key already exists
        for existing_pair in chain: 
            if existing_pair.key == key:
                existing_pair.value = value # Update existing value
                return # Key found and updated, no need to add new pair
        
        # If key not found in chain, append new pair
        chain.append(Pair(key, value))
        self.size += 1 # Increment total size of elements in map

        # Check load factor and rehash if necessary
        # Using float division for accuracy
        if self.size / self.capacity >= self.load_factor_threshold: 
            self.rehash()
       
    def get(self, key: int) -> int:
        index = self.hash(key)
        chain = self.buckets[index]

        # Iterate through the chain to find the key
        for pair in chain : 
            if pair.key == key : # No need for 'if pair' as chain elements are Pair objects
                return pair.value
        
        return -1 # Key not found in the chain
        
    def remove(self, key: int) -> None:
        index = self.hash(key)
        chain = self.buckets[index]

        # Iterate through the chain to find and remove the key
        # Use enumerate to get both index and pair for deletion
        for i, pair in enumerate(chain) : 
            if pair.key == key : # No need for 'if pair'
                del chain[i] # Correctly remove the element from the list
                self.size -= 1 # Decrement total size
                return # Key found and removed, nothing more to do