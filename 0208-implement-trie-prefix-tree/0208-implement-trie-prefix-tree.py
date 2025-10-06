class TrieNode : 
    def __init__(self) : 
        self.children = {}
        self.word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root 
        for c in word : 
            if c not in cur.children : 
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.root 
        for c in word : 
            if c not in cur.children : return False
            cur = cur.children[c]
        return cur.word

    def startsWith(self, prefix: str) -> bool:
        def dfs(node , index) : 
            if index == len(prefix) : 
                return True 
            
            if prefix[index] in node.children : 
                return dfs(node.children[prefix[index]] , index+1)
            
            return False
        return dfs(self.root , 0)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)