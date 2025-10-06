class TrieNode : 
    def __init__(self) : 
        self.children = {}
        self.eow = False

class Trie : 
    def __init__(self) : 
        self.root = TrieNode()
        self.root.eow = True
    
    def insert(self, word) : 
        cur = self.root
        for c in word : 
            if c not in cur.children : 
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.eow = True 
    
    def search(self, word) : 
        cur = self.root
        for c in word : 
            if c not in cur.children : return False 
            cur = cur.children[cur]
        return cur.word 
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for w in words : 
            trie.insert(w)
        
        cand , l = [] , 0
        explore = deque([(trie.root , [''])])
        while explore : 
            node , path = explore.pop()
            if not node.eow : continue 
            if len(path) > l : 
                cand = path
                l = len(path)
            for c in reversed(string.ascii_lowercase) : 
                if c in node.children : 
                    explore.append((node.children[c] , path+[c]))
        return ''.join(cand)
