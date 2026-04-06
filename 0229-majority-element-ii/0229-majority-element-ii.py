class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = math.floor(len(nums)/3)
        counter = Counter(nums)
        return [num for num , count in counter.items() if count > majority]
        