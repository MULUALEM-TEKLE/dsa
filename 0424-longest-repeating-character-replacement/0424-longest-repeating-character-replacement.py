class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = defaultdict(int)
        left = 0 
        longest = 0

        for right in range(len(s)) : 
            cnt[s[right]] += 1 
            while (right-left+1) - max(cnt.values()) > k : 
                cnt[s[left]] -= 1 
                left += 1 
            longest = max(longest , right-left+1)
        return longest