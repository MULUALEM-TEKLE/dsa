class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        prefix_len = len(prefix)

        for word in strs[1:] : 
            while prefix != word[: prefix_len] :
                if prefix_len == 0 : return ""
                prefix_len -= 1
                prefix = prefix[0 : prefix_len]
                
        return prefix

        # shortest_len = min(len(s) for s in strs)

        # for i in range(shortest_len):
        #     char = strs[0][i]
        #     for j in range(1, len(strs)):
        #         if  strs[j][i] != char : 
        #             return strs[0][:i]
        # return strs[0][:shortest_len]
        