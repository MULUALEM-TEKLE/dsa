'''
-> given an array of distinct integers candidates and a target integer target, 
-> return a list of all unique combinations of candidates where the chosen numbers sum to target. 
    -> You may return the combinations in any order.
    -> The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.


'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        comb = []

        def dfs(i , cur) : 
            
            if cur == target : 
                res.append(comb[:])
                return
            
            if cur > target : 
                return
            
            if i >= len(candidates) : 
                return
            
            comb.append(candidates[i])
            dfs(i , cur + candidates[i])
            comb.pop()
            dfs(i+1 , cur) 
                   
        dfs(0 , 0)
        return res 