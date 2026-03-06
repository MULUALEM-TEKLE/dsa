class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_counter = Counter(s1)
        match_needed = len(target_counter)
        matched_count = 0 
        window_counter = Counter()
        left = 0 

        for right in range(len(s2)) : 
            right_char = s2[right]
            window_counter[right_char] += 1 
            
            if right_char in target_counter and window_counter[right_char] == target_counter[right_char] : 
                matched_count += 1 
             
            while  right-left+1 > len(s1) : 
                left_char = s2[left]
                if left_char in target_counter and window_counter[left_char] == target_counter[left_char] : 
                    matched_count -= 1 
                window_counter[left_char] -= 1 
                left += 1 
        
            if matched_count == match_needed : 
                return True 

        return False