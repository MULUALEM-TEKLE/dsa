from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        s_bytes = bytearray(s.encode("utf-8"))
        N = len(s_bytes)

        def reverse_segment(arr: bytearray, left: int, right: int):
            """Reverse a segment of the bytearray from index left to right."""
            if left < 0 or right >= len(arr) or left >= right:
                return
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        def clean_spaces(arr: bytearray) -> int:
            """Remove extra spaces and return the effective length of the cleaned array."""
            left, right = 0, 0
            
            # Skip leading spaces
            while right < N and arr[right] == ord(' '):
                right += 1

            while right < N:
                # Copy word characters
                while right < N and arr[right] != ord(' '):
                    arr[left] = arr[right]
                    left += 1
                    right += 1
                
                # Skip multiple spaces
                while right < N and arr[right] == ord(' '):
                    right += 1
                
                # Add a single space only if there are more non-space characters
                if right < N:
                    arr[left] = ord(' ')
                    left += 1
            
            # No need to trim trailing space, as we only add space when more words follow
            return left

        effective_len = clean_spaces(s_bytes)

        if effective_len == 0:
            return ""

        # Reverse the entire cleaned string
        reverse_segment(s_bytes, 0, effective_len - 1)

        # Reverse each word
        word_start = 0
        i = 0
        while i < effective_len:
            if s_bytes[i] == ord(' ') or i == effective_len - 1:
                # If at a space, reverse up to the character before the space
                # If at the end, include the last character
                end = i - 1 if s_bytes[i] == ord(' ') else i
                reverse_segment(s_bytes, word_start, end)
                word_start = i + 1
                i += 1
            else:
                i += 1

        # Decode only the effective portion of the bytearray
        return s_bytes[:effective_len].decode("utf-8")

