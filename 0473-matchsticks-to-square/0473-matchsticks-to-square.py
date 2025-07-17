'''
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick.
-> total number of matchsticks -> small
-> length of matchsticks[i] -> large



You want to use all the matchsticks to make one square.
-> all must be used, the end of the array must be reached
-> must make a square
    -> square is divisible by 4 -> return false if sum(matchsticks)//4 != 0
    -> so this is a matter of dividing the array into equal 4 parts until the end of the array is reached
    -> equal parts that adds up to a square
    -> a single side should be sum(matchsticks)//4

You should not break any stick, 
but you can link them up, 
    -> I can add them up -> 2 or more matchsticks can make up a side
and each matchstick must be used exactly one time.
    -> can not reuse a matchstick

Return true if you can make this square and false otherwise.

Examples : 
Input: matchsticks = [1,1,2,2,2]
->sum = 8 -> maybe possible
Output: true

lets have a sides container 
[0, 0, 0, 0]
side_len = sum//4 = 2 
-> for container[0] go through matchsticks until its sum == 2 
-> I think sorting the matchsticks is a good idea, also reverse so its a good idea to prune early 



Input: matchsticks = [3,3,3,3,4]
sum = 16 -> maybe possible
Output: false

strategy : 
I could try to build 4 equal sides
iterate through everything and try to build 4 equal sides, 
if I manage to cover all elements while getting 4 equal sides I think I can do that 

param = i
basecase 
if i == len(matchsticks) : return True

for side in range(4)
    if matchstick + sides[side] <= min_side_len : 
        sides[side] += matchstick
        if  recurse(i+1) : 
            return True 
        sides[side] -= matchstick 
return False
'''


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matches = matchsticks
        total_sum = sum(matches)
        if total_sum%4 != 0 : return False
        side_length = total_sum//4
        container = [0] * 4 
        matches.sort(reverse=True)
        # @cache
        def dfs(i):
            if i == len(matches) : return True 
            
            for side in range(4) : 
                if container[side] + matches[i] <= side_length :
                    container[side] += matches[i]
                    if dfs(i+1) : return True 
                    container[side] -= matches[i]

            return False
        
        return dfs(0)