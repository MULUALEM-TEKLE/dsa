class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 0

        while i < len(words)-1 : 
            if Counter(words[i]) == Counter(words[i+1]) : 
                del words[i+1]
                continue
            i+=1 
        
        return words