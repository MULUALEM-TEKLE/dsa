class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        left = 0
        def sort_word(word) : 
            word = list(word)
            word.sort()
            word = "".join(word)
            return word 
        p = sort_word(p)
        N = len(p)
        while left < len(s)-N+1 : 
            if s[left] in p and sort_word(s[left : left+N]) == p : 
                res.append(left)
                left += 1
            else : 
                left += 1 
            
        return res 