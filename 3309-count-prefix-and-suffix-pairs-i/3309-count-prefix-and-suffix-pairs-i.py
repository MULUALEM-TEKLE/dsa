class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2) :
            # print(f'checking {str1} and {str2}')
            # if str2[:len(str1)] == str1 and str2[:-(len(str1)-1)] == str1 : 
            # print(f"{str2[:len(str1)]} == {str1} and {str2[:-(len(str1))]} == {str1}")
            return str2[:len(str1)] == str1 and  str2[-(len(str1)):] == str1

        count = 0 
        for i in range(len(words)) : 
            for j in range(i+1 ,len(words)) : 
                if len(words[i]) > len(words[j]) : continue
                if isPrefixAndSuffix(words[i], words[j]) : count += 1
        
        return count 

        # a = "a"
        # aab = "aab"
        # print(aab[-1:])