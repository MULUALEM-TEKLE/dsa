class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = defaultdict(int)

        for letter in s : 
            freq[letter] += 1 
        
        for index , letter in enumerate(s) : 
            if freq[letter] == 1 : 
                return index

        return -1