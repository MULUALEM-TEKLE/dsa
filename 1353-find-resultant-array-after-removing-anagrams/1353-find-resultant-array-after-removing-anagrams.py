class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        idx_to_keep = []
        i = 1
        while i < len(words): 
            if Counter(words[i]) == Counter(words[i-1]) : 
                del words[i]
                continue
            i += 1
        return words
                