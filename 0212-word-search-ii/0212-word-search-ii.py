class TrieNode : 
    def __init__(self) : 
        self.children = {}
        self.word = False
        self.refs = 0

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root 
        cur.refs += 1
        for c in word : 
            if c not in cur.children : 
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.word = True
    
    def remove(self , word) : 
        cur = self.root 
        cur.refs -= 1 

        for c in word : 
            if c in cur.children :
                cur = cur.children[c] 
                cur.refs -= 1 




class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows , cols = len(board) , len(board[0])
            
        res = set()
        visited = set()

        trie = Trie()
        for word in words :
            trie.insert(word)

        def dfs(r , c , node , word) : 
            if (
                r not in range(rows) 
                or c not in range(cols) 
                or (r , c) in visited 
                or board[r][c] not in node.children 
                or node.children[board[r][c]].refs < 1
                ) : 
                return 

           
            visited.add((r , c)) 
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.word : 
                node.word = False 
                res.add(word)
                trie.remove(word)

            dfs(r+1 , c , node , word)
            dfs(r-1 , c , node , word)
            dfs(r , c+1 , node , word)
            dfs(r , c-1 , node , word)
           
            visited.remove((r , c))

        for r in range(rows) : 
            for c in range(cols) :     
                dfs(r , c , trie.root , "")

        return list(res)
        
      