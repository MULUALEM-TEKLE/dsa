class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        maxlen = 0 
        for right in range(len(s)) : 
            while s[right] in window : 
                window.remove(s[left])
                left += 1  
            window.add(s[right])
            maxlen = max(maxlen , len(window))
        return maxlen