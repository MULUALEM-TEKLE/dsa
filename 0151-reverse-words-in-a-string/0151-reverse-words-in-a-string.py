from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        # Convert string to list of characters for in-place manipulation
        chars = list(s)
        N = len(chars)

        def reverse_segment(arr: list, left: int, right: int):
            """Reverse a segment of the list from index left to right."""
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        # Clean spaces and get effective length in one pass
        left = 0
        right = 0
        while right < N:
            # Skip leading or multiple spaces
            while right < N and chars[right] == ' ':
                right += 1
            # Copy word
            while right < N and chars[right] != ' ':
                chars[left] = chars[right]
                left += 1
                right += 1
            # Add single space if more characters exist
            if right < N and left > 0:
                chars[left] = ' '
                left += 1
            right += 1

        # Trim trailing space if present
        effective_len = left - 1 if left > 0 and chars[left - 1] == ' ' else left
        if effective_len <= 0:
            return ""

        # Reverse the entire cleaned string
        reverse_segment(chars, 0, effective_len - 1)

        # Reverse each word
        word_start = 0
        for i in range(effective_len):
            if chars[i] == ' ':
                reverse_segment(chars, word_start, i - 1)
                word_start = i + 1
        # Reverse the last word
        reverse_segment(chars, word_start, effective_len - 1)

        # Join the list back to a string
        return ''.join(chars[:effective_len])