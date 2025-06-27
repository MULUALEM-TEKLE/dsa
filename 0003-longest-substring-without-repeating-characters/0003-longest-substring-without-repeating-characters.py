class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxlen = 0 

        lookup = {}

        for i,c in enumerate(s) : 
            if c in lookup and start <= lookup[c] : 
                start = lookup[c] + 1 
            else : 
                maxlen = max(maxlen , i - start + 1)
            lookup[c] = i

        return maxlen