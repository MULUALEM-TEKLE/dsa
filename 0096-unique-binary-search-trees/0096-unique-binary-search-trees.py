class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 : return 0
        @cache
        def count(nodes) : 
            if nodes <= 1 : 
                return 1 
            
            cnt = 0 

            for i in range(1, nodes+1) : 
                left_ways = count(i-1)
                right_ways = count(nodes-i)

                cnt += left_ways * right_ways
            
            return cnt
        
        return count(n)