class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, num in enumerate(nums) : 
            if num in map : 
                map[num].append(index)
            else : 
                map[num] = [index]

        for num in nums : 
            if target - num in map  :
                print(map[num])
                if num == target-num and len(map[num]) == 2 : 
                    return map[num] 
                if map[target-num] != map[num] :
                    return [map[num][0] , map[target-num][0]]