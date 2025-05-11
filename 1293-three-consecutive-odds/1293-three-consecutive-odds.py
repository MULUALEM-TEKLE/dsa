class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        total_odds_found = 0
        for i in range(len(arr)):
            if arr[i] % 2 != 0 : 
                total_odds_found += 1 
                if total_odds_found == 3:
                    return True
            else : 
                total_odds_found = 0 
        return False



        