class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "" : 
            return 0 
        window = set()
        window.add(s[0])
        left = 0
        longest = 1 

        for right in range(1 , len(s)) : 
            while s[right] in window : 
                window.remove(s[left])
                left += 1 
            
            window.add(s[right])
            longest = max(longest ,right-left+1)
        
        return longest