class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_counter = Counter(s1)
        window_len = len(s1)
        for i in range(len(s2)) : 
            if Counter(s2[i : i+window_len]) == target_counter : return True
        return False