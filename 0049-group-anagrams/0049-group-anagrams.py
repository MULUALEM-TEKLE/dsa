class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}

        for word in strs : 
            sorted_word = "".join(sorted(word))
            if sorted_word in table:
                table[sorted_word].append(word)
            else : 
                table[sorted_word] = [word]
        return [vals for vals in table.values()] 
