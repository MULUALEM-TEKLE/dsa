# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         p_table = Counter(p)
#         N = len(p)
#         left = 0
#         res = []
#         window_table = {}
#         while left < len(s)-N+1 : 
#             if s[left] not in p : 
#                 left += 1 
#                 continue 
#             window_table = Counter(s[left : left+N])
#             if window_table == p_table : 
#                 res.append(left)
#             # window_table = {}
#             left += 1 
#         return res 

from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        
        # Edge case: if p is longer than s, no anagram can exist
        if len(p) > len(s):
            return res

        # 1. Create frequency map for pattern p
        p_count = Counter(p)
        
        # 2. Create frequency map for the initial window in s (first len(p) characters)
        window_count = Counter(s[:len(p)])

        # 3. Check the initial window
        if p_count == window_count:
            res.append(0) # If it matches, add index 0

        # 4. Slide the window
        # 'left' pointer starts at 0, 'right' pointer starts at len(p)
        # The loop iterates 'right' from len(p) up to len(s) - 1
        for right in range(len(p), len(s)):
            # Character entering the window from the right
            incoming_char = s[right]
            window_count[incoming_char] += 1

            # Character leaving the window from the left
            outgoing_char_index = right - len(p) # This is the 'left' pointer's position for this window
            outgoing_char = s[outgoing_char_index]
            window_count[outgoing_char] -= 1

            # If a character's count becomes 0, it's good practice to remove it from the map
            # This ensures that 'Counter' comparisons work correctly (e.g., {'a': 0} != {})
            if window_count[outgoing_char] == 0:
                del window_count[outgoing_char]
            
            # Check if the current window is an anagram
            if p_count == window_count:
                # The starting index of this window is 'outgoing_char_index + 1'
                res.append(outgoing_char_index + 1)
                
        return res