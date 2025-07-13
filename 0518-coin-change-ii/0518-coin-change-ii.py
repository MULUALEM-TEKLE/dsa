class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def ways(i,amt) : 
            if amt == 0 : return 1 
            if i == len(coins) or amt < 0 : return 0
            if (i,amt) in memo : return memo[(i,amt)]
            memo[(i,amt)] = ways(i , amt-coins[i]) + ways(i+1 , amt)
            return memo[(i,amt)]
        res = ways(0 , amount)
        # print(memo)
        return res
            