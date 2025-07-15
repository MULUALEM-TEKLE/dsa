# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         coins.append(0)
#         coins.sort()
#         dp = [[0]*(amount+1 )for _ in range(len(coins))]
#         rows , cols = len(dp) , len(dp[0])
#         for j in range(1 , amount+1) : 
#             if j < coins[1] :   
#                 dp[0][j] = float('inf')
#         print(dp)
#         dp[0][0] = 0
#         for j in range(1 , amount+1) : 
#             if coins[1] <= j :   
#                 dp[0][j] = dp[0][j-coins[1]]+1
#         for row in range(1 , rows) : 
#             for col in range(cols) : 
#                 if col >= coins[row] : 
#                     dp[row][col] = min(dp[row-1][col] , 1 + dp[row][col-coins[row]])
#                 else : 
#                     dp[row][col] = dp[row-1][col] 
                
#         return dp[rows-1][cols-1] if dp[rows-1][cols-1] != float('inf') else -1 

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Sort coins. While not strictly necessary for correctness in 2D DP,
        # it can sometimes help with understanding or minor optimizations (like early breaks
        # if amounts are small and coins are large, though not explicitly used here).
        coins.sort()

        # dp[i][j] will store the minimum number of coins needed to make amount 'j'
        # using only the first 'i' types of coins (coins[0] to coins[i-1]).
        #
        # Rows: len(coins) + 1 (for considering 0 to len(coins) types of coins)
        # Cols: amount + 1 (for amounts from 0 to 'amount')
        num_coin_types = len(coins)
        dp = [[float('inf')] * (amount + 1) for _ in range(num_coin_types + 1)]

        # Base Case 1: To make an amount of 0, 0 coins are always needed.
        # This holds true regardless of how many coin types we consider.
        # dp[i][0] = 0 for all i (from 0 to num_coin_types)
        for i in range(num_coin_types + 1):
            dp[i][0] = 0

        # Fill the DP table using a bottom-up approach
        # Outer loop: Iterate through each coin type available
        # 'i' represents the count of coin types considered so far (1-indexed).
        # So, 'coins[i-1]' is the current coin being evaluated.
        for i in range(1, num_coin_types + 1):
            current_coin_value = coins[i-1] # Get the value of the current coin type from the original list

            # Inner loop: Iterate through each possible amount from 1 up to the target amount
            # 'j' represents the current amount we are trying to make.
            for j in range(1, amount + 1):
                # Option 1: Do NOT use the current coin type (coins[i-1])
                # In this case, the minimum coins needed to make amount 'j' is the same
                # as if we only used the previous 'i-1' coin types.
                dp[i][j] = dp[i-1][j]

                # Option 2: Use the current coin type (coins[i-1])
                # This option is only possible if the current amount 'j' is
                # greater than or equal to the value of the current coin.
                if j >= current_coin_value:
                    # If we use 'current_coin_value', we need 1 coin (the current one)
                    # plus the minimum coins to make the remaining amount (j - current_coin_value).
                    # We look up dp[i][j - current_coin_value] because the current coin type
                    # can be used multiple times (unbounded knapsack problem variant).
                    
                    # Ensure that the subproblem (j - current_coin_value) was reachable.
                    # If dp[i][j - current_coin_value] is still float('inf'), it means
                    # that remaining amount is not possible with current/previous coins,
                    # so adding 1 to it would still be infinity.
                    if dp[i][j - current_coin_value] != float('inf'):
                        dp[i][j] = min(dp[i][j], 1 + dp[i][j - current_coin_value])
        
        # The final result is stored at dp[num_coin_types][amount].
        # This cell contains the minimum coins to make 'amount' using all available coin types.
        final_result = dp[num_coin_types][amount]

        # If the final result is still float('inf'), it means the amount cannot be made
        # with the given coins. In this case, return -1 as per problem requirements.
        if final_result == float('inf'):
            return -1
        else:
            return final_result

