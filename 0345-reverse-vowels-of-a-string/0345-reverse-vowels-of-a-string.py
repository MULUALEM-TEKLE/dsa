class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u' , "A" , "E" , "I", "O" , "U"]
        s_v  = []

        for letter in s: 
            if letter in vowels : 
                s_v.append(letter)
        
        print(s_v)

        right = len(s_v) - 1 
        res = ""
        for index , letter in enumerate(s) : 
            if letter in vowels : 
                res += s_v[right]
                right -= 1
            else : 
                res += letter

        return res

