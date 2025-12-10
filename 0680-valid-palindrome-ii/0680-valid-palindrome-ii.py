class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(test) : 
            left , right = 0 , len(test)-1
            while left <= right : 
                if test[left] != test[right] : 
                    return False 
                left += 1
                right -= 1 
            return True 
        
        left , right = 0 , len(s)-1
        while left <= right : 
            if s[left] != s[right] : 
                if isPalindrome(s[left+1 : right+1]) or isPalindrome(s[left : right]) : 
                    return True
                else : 
                    return False
            left += 1 
            right -= 1
        return True