class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_len = len(word1)
        w2_len = len(word2)

        longest_string = word1

        if w2_len > w1_len:
            longest_string = word2

        merged_string = ""
        for i in range(min(w1_len, w2_len)):
            
            if word1[i] and word2[i]:
                merged_string += word1[i]
                merged_string += word2[i]

        if(w1_len != w2_len):
            merged_string += longest_string[-abs(w1_len - w2_len ) : len(longest_string) ]

        return merged_string


        