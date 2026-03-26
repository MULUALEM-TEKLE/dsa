class Solution:
    def longestWord(self, words: List[str]) -> str:
        safe = {""}
        longest = ""

        words.sort()

        for word in words : 
            if word[:-1] in safe : 
                safe.add(word)
            
                if len(word) > len(longest) : 
                    longest = word
        
        return longest 