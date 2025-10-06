class TrieNode : 
    def __init__(self) : 
        self.children = {}
        self.eow = False

class Trie : 
    def __init__(self) : 
        self.root = TrieNode()
    
    def insert(self, word) : 
        cur = self.root
        for c in word : 
            if c not in cur.children : 
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.eow = True 
    
    def search(self, word) : 
        cur = self.root
        path = []
        for c in word : 
            if c not in cur.children : return None
            cur = cur.children[c]
            path.append(c)
            if cur.eow : 
                return "".join(path)
        return None

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary : 
            trie.insert(word)
        
        sentence = sentence.split(" ")
        
        for i,w in enumerate(sentence) : 
            found = trie.search(w)
            if found: 
                sentence[i] = found

        return " ".join(sentence)