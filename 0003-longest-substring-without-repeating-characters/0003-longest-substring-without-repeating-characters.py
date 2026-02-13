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
            longest = max(longest , right-left+1)
            window.add(s[right])
        
        return longest