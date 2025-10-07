class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0 
        for i in range(len(words)) : 
            for j in range(i+1 ,len(words)) :
                w1 = words[i]
                w2 = words[j] 
                L = len(w1)
                if len(w1) > len(w2) : continue
                if w2.startswith(w1) and w2.endswith(w1) : count += 1
        
        return count 
