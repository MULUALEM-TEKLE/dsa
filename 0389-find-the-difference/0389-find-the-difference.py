class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_table = defaultdict(int)
        s_table = defaultdict(int)

        for letter in s : 
            s_table[letter] += 1 

        for letter in t : 
            t_table[letter] += 1 

        for letter in t : 
            if t_table[letter] != s_table[letter] : 
                return letter