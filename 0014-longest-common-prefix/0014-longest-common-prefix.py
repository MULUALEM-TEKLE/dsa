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
        