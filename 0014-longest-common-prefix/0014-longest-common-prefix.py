class TrieNode : 
    def __init__(self) : 
        self.children = {}
        self.eof = False 

class Trie : 
    def __init__(self) : 
        self.root = TrieNode()
    
    def insert(self , word) : 
        cur = self.root 
        for c in word : 
            if c not in cur.children : 
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.eof = True 
    
    def find_longest_prefix(self) : 
        prefix = ""
        cur = self.root 

        while len(cur.children) == 1 and not cur.eof : 
            char = list(cur.children.keys())[0]
            prefix += char 
            cur = cur.children[char]
        
        return prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs : return ""

        trie = Trie()
        for word in strs : 
            trie.insert(word)
        
        return trie.find_longest_prefix()
        