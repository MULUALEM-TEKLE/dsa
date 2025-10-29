class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0 
        left = 0
        counts = defaultdict(int)
        maxf = 0

        for right in range(len(s)) : 
            counts[s[right]] +=1
            maxf = max(maxf , counts[s[right]])
            while (right-left+1) - maxf > k : 
                counts[s[left]] -= 1
                left += 1 
            longest = max(longest , right-left+1)
        
        return longest