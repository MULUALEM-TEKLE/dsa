class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t : return s
        target_counter = Counter(t)
        matched_count = 0 
        match_needed = len(target_counter)

        window_counter = Counter()
        res = ""
        left = 0 

        for right in range(len(s)) : 
            char = s[right]
            window_counter[char] += 1 
            if char in target_counter and target_counter[char] == window_counter[char] : 
                matched_count += 1 
            
            while matched_count == match_needed : 
                cur_size = right - left + 1 

                if not res or cur_size < len(res) : 
                    res = s[left : right+1]
                
                left_char = s[left]

                if left_char in target_counter and target_counter[left_char] == window_counter[left_char] : 
                    matched_count -= 1 
                

                window_counter[left_char] -= 1
                left += 1 

        return res 