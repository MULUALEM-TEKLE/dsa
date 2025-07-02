from collections import Counter
from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if not words:
            return []

        # Initialize the result list with the first word
        # It's guaranteed to be unique relative to anything before it
        result = [words[0]]
        
        # Keep track of the Counter for the last added word in 'result'
        # This avoids recomputing it repeatedly
        last_word_counter = Counter(words[0])

        # Iterate from the second word onwards
        for i in range(1, len(words)):
            current_word = words[i]
            current_word_counter = Counter(current_word)

            # Compare the current word's counter with the last added word's counter
            if current_word_counter != last_word_counter:
                # If they are not anagrams, add the current word to the result
                result.append(current_word)
                # Update the last_word_counter for the next comparison
                last_word_counter = current_word_counter
            # Else (if they are anagrams), do nothing, effectively "skipping" the current word
            
        return result