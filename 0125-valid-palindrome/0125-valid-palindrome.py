class Solution:
    def isPalindrome(self, s: str) -> bool:
        retutn s == s[::-1]