class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}

        for index, word in enumerate(["".join(sorted(s)) for s in strs]) : 
            if word in table.keys() : 
                table[word].append(strs[index])
            else : 
                table[word] = [strs[index]]

        return list(table.values())
