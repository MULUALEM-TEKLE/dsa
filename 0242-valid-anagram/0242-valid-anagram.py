class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case
        # if their lengths are not the same return false
        if len(s) != len(t) : 
            return False
        # approach one
        # else construct two tables with word frequencies and add letters as keys with values of frequencies
        # compare for a letter frequencies and if all are equal return true, if not return false
        s_table = {}
        t_table = {}

        for letter in s :
            if letter in s_table.keys() : 
                s_table[letter] += 1
            else : 
                s_table[letter] = 1
        
        for letter in t :
            # if letter not in s_table.keys() : 
            #     return False

            if letter in t_table.keys() : 
                t_table[letter] += 1
            else : 
                t_table[letter] = 1

        for letter in s : 
            if letter not in s_table.keys() or letter not in t_table.keys() : 
                return False
            
            if s_table[letter] != t_table[letter]:
                return False
        
        return True




        # approach 4
        # just sort the compare
        # t = sorted(t)
        # s = sorted(s)
        # return t == s
        