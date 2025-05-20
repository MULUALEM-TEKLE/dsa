class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       
        return len([s for s in s.split(" ") if s != ""][-1]) 
       