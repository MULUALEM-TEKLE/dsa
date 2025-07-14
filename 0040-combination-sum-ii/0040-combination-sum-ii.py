from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort candidates to handle duplicates and ensure combinations are unique
        # when converted to tuples later (e.g., (1,2) vs (2,1))
        candidates.sort()

        # dp[i] will be a set of tuples, where each tuple represents a unique
        # combination that sums up to 'i'. Using a set of tuples automatically
        # handles uniqueness of combinations.
        dp = [set() for _ in range(target + 1)]

        # Base case: To make sum 0, there is one way: an empty combination.
        # We represent an empty combination as an empty tuple.
        dp[0].add(()) # Add an empty tuple to the set for amount 0

        # Iterate through each number in the sorted candidates list
        # This loop structure is crucial for "each number used at most once".
        # By iterating through candidates first, and then amounts, we ensure
        # that when we consider adding a 'num', we are only extending combinations
        # that were formed *without* using this specific 'num' instance yet.
        for num in candidates:
            # Iterate through amounts from 'target' down to 'num'.
            # We go downwards to ensure that 'num' is used at most once for each path
            # (i.e., we don't use dp[j - num] that already incorporated 'num' from this iteration).
            for j in range(target, num - 1, -1):
                # If there are combinations for the amount 'j - num'
                if dp[j - num]:
                    # For each existing combination that sums to 'j - num'
                    for prev_comb in dp[j - num]:
                        # Create a new combination by adding the current 'num'
                        new_comb = prev_comb + (num,) # Add num to the tuple

                        # Sort the new tuple to ensure uniqueness regardless of insertion order.
                        # E.g., (1,2) and (2,1) become the same after sorting to (1,2).
                        # This is important because the problem asks for unique combinations,
                        # not unique permutations.
                        sorted_new_comb = tuple(sorted(new_comb))
                        
                        # Add the sorted unique combination to the set for amount 'j'
                        dp[j].add(sorted_new_comb)
        
        # Convert the set of tuples for the target amount into a list of lists
        # Each tuple in dp[target] is a unique combination.
        result = [list(comb) for comb in dp[target]]
        
        return result

