class Solution:
    def rob(self, nums: List[int]) -> int:
        one = two = 0

        for n in nums : 
            tmp = max(n + one , two)
            one = two 
            two = tmp 
        return two