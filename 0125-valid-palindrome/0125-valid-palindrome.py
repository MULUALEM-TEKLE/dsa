class Solution:
    def isPalindrome(self, s: str) -> bool:
        test_str = "".join(c for c in s if c.isalnum())
        test_str = test_str.lower()
        left , right = 0 , len(test_str)-1

        while left <= right : 
            if test_str[left] == test_str[right] : 
                left += 1 
                right -= 1 
            else : 
                return False 
        return True