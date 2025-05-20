class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle : 
            return 0
        
        if len(needle) > len(haystack) : 
            return -1

        pos = -1
        needle_ptr = 0

        for index, letter in enumerate(haystack) : 
            if letter == needle[needle_ptr] and len(needle) > 1 : 
                pos = index
                needle_ptr += 1
                while index + needle_ptr <= len(haystack) - 1 and needle[needle_ptr] == haystack[index + needle_ptr] : 
                    if needle_ptr == (len(needle) -1) : 
                        return pos

                    needle_ptr += 1

                    if index + needle_ptr > len(haystack) - 1 : 
                        return -1

                pos = -1
                needle_ptr = 0  
            elif letter == needle[needle_ptr] and len(needle) == 1 :  
                return index  

        return -1
        