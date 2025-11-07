class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        if s == "" : return 0
        window.add(s[0])
        longest = 1
        left = 0

        for right in range(1 , len(s)) : 
            while s[right] in window : 
                window.remove(s[left])
                left += 1 
            window.add(s[right])
            longest = max(longest , len(window))
        
        return longest