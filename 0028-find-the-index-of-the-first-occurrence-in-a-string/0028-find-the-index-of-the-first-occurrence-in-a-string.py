class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if haystack == needle : 
        #     return 0
        
        # if len(needle) > len(haystack) : 
        #     return -1
        


        # pos = -1
        # needle_ptr = 0

        # for index in range(len(haystack)) : 
        #     if haystack[index] == needle[needle_ptr] and len(needle) > 1 : 
        #         pos = index
        #         needle_ptr += 1
        #         while index + needle_ptr <= len(haystack) - 1 and needle[needle_ptr] == haystack[index + needle_ptr] : 
        #             if needle_ptr == (len(needle) -1) : 
        #                 return pos

        #             needle_ptr += 1

        #         pos = -1
        #         needle_ptr = 0  
        #     elif haystack[index] == needle[needle_ptr] and len(needle) == 1 :  
        #         return index  

        # return pos

        if needle == "" or haystack == "" : 
            return -1

        for i in range(len(haystack) - len(needle) + 1 ) : 
            if haystack[i : i + len(needle)] == needle : 
                return i

        return -1
        