class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = strs.pop()
        prefix_len = len(prefix)

        for word in strs : 
            while prefix != word[: prefix_len] :
                if prefix_len == 0 : return ""
                prefix_len -= 1
                prefix = prefix[0 : prefix_len]
                
        return prefix
        