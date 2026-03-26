class TrieNode : 
    def __init__(self) : 
        self.children = {}
        self.eow = False 
        self.value = ""

class Trie : 
    def __init__(self) :
        self.root = TrieNode()

    def insert(self , word) : 
        cur = self.root 

        for c in word : 
            if c not in cur.children : 
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.eow = True 
        cur.val = word 
    
    def bfs(self) : 
        q = deque()
        q.append(self.root)
        res = ""

        while q : 
            node = q.popleft()

            for child in node.children.values() : 
                if child.eow : 
                    if len(child.val) > len(res) : 
                        res = child.val
                    q.append(child)
        
        return res
        


class Solution:
    def longestWord(self, words: List[str]) -> str:
        t = Trie()
        words.sort()
        for word in words : 
            t.insert(word)
        
        return t.bfs()