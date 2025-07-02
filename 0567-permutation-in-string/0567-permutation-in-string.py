class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)

        N = len(s1)
        left = 0
        while left < len(s2)-N+1 : 
            if Counter(s2[left:left+N]) == s1_counter : 
                return True
            left += 1 
        return False