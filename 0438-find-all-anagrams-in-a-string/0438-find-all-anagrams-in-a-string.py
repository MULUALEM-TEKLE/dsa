from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)
        
        # If p is longer than s, no anagram can exist.
        if p_len > s_len:
            return []

        # Frequency map for pattern p
        p_count = Counter(p)
        
        # Frequency map for the initial window of s
        s_window_count = Counter(s[:p_len])
        
        # List to store starting indices of anagrams
        result_indices = []

        # 'matches' will count how many characters have the exact required frequency
        # between s_window_count and p_count.
        # An anagram is found when 'matches' equals the number of unique characters in p.
        matches = 0
        for char_code in range(ord('a'), ord('z') + 1):
            char = chr(char_code)
            if s_window_count[char] == p_count[char]:
                matches += 1

        # Check the initial window
        # An anagram is found if all character counts match.
        # This is equivalent to `s_window_count == p_count` but done with `matches`.
        if matches == 26: # Assuming lowercase English alphabet (26 characters)
            result_indices.append(0)

        # Slide the window across s
        # The window starts at index 0 and ends at p_len-1.
        # For each iteration, the window shifts one position to the right.
        # 'i' represents the starting index of the current window.
        # The loop runs from i=1 up to s_len - p_len.
        for i in range(1, s_len - p_len + 1):
            # Character leaving the window: s[i-1]
            left_char = s[i-1]
            # Character entering the window: s[i + p_len - 1]
            right_char = s[i + p_len - 1]

            # Update 'matches' for the character leaving the window
            # Before decrementing: if it was a perfect match, it's about to break.
            if s_window_count[left_char] == p_count[left_char]:
                matches -= 1
            s_window_count[left_char] -= 1
            # After decrementing: if it now becomes a perfect match (e.g., was over-counted), increment.
            if s_window_count[left_char] == p_count[left_char]:
                matches += 1

            # Update 'matches' for the character entering the window
            # Before incrementing: if it was a perfect match, it's about to break.
            if s_window_count[right_char] == p_count[right_char]:
                matches -= 1
            s_window_count[right_char] += 1
            # After incrementing: if it now becomes a perfect match, increment.
            if s_window_count[right_char] == p_count[right_char]:
                matches += 1

            # Check if the current window is an anagram
            # All character counts must perfectly match.
            if matches == 26: # Still assuming lowercase English alphabet (26 characters)
                result_indices.append(i)
                
        return result_indices

