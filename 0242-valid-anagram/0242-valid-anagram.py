class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case
        # if their lengths are not the same return false
        if len(s) != len(t) : 
            return False
        # approach one
        # else construct one table and add letters as keys with index
        # compare for a letter in one of the strings check if exists in the other's table
        # if all letters are in the other then you're done 
        # approach 2
        # of just looping works too
        # approach 3 
        # maybe using a sorted set and then comparing  the sets  might work too 
        # approach 4
        # just sort the compare

        t = sorted(t)
        s = sorted(s)
        return t == s
        