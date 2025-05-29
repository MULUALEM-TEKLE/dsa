class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_freq = {}
        ransom_freq = {}

        for letter in magazine : 
            if letter in magazine_freq.keys() : 
                magazine_freq[letter] += 1 
            else : 
                magazine_freq[letter] = 1

        for letter in ransomNote : 
            if letter in ransom_freq.keys() : 
                ransom_freq[letter] += 1 
            else : 
                ransom_freq[letter] = 1
        
        for letter in ransomNote : 
            if letter not in magazine_freq.keys() or ransom_freq[letter] > magazine_freq[letter] : 
                return False

        return True
        