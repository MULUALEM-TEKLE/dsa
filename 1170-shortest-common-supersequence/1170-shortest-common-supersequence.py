class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m , n = len(str1) , len(str2)
        # self.res = "X" * (m+n+1)
        # @cache
        # def explore(i, j , cur) : 
            
        #     if i == m : 
        #         cur += str2[j:]
        #         if len(cur) < len(self.res) : self.res = cur
        #         return
        #     if j == n : 
        #         cur += str1[i:]
        #         if len(cur) < len(self.res) : self.res = cur
        #         return
            
        #     if str1[i] == str2[j] : 
        #         explore(i+1 , j+1 , cur + str1[i])
        #     else : 
        #         explore(i+1 , j , cur + str1[i])
        #         explore(i, j+1 , cur + str2[j])
        
        # explore(0 , 0 , "")

        # return self.res

        # dp = [[""] *(n+1) for _ in range(m+1) ]
        # for i in range(m+1) : 
        #     dp[i][-1] = str1[i:]
        # for i in range(n+1) : 
        #     dp[-1][i] = str2[i:]
        # print(dp)

        # '''
        # [    a.      b.      c. 
        #  c  ['',     '',     '',     'cab'], 
        #  a  ['',     '',     '',     'ab'], 
        #  b  ['',     '',     '',     'b'], 
        #     ['abc', 'bc',    'c',    '']]
        # '''

        # for i in reversed(range(m)) : 
        #     for j in reversed(range(n)) : 
        #         if str1[i] == str2[j] : 
        #             dp[i][j] = str1[i] + dp[i+1][j+1]
        #         else : 
        #             res1 = str1[i] + dp[i+1][j]
        #             res2 = str2[j] + dp[i][j+1]
        #             dp[i][j] = res1 if len(res1) < len(res2) else res2
        # return dp[0][0]

        prev = [str2[i:] for i in range(n)]
        # print(prev)
        prev.append("")

        for i in reversed(range(m)) : 
            cur = [""] * n
            cur.append(str1[i:])
            # print(cur)
            for j in reversed(range(n)) : 
                if str1[i] == str2[j] : 
                    cur[j] = str1[i] + prev[j+1]
                else : 
                    res1 , res2 = str1[i] + prev[j] , str2[j] + cur[j+1]
                    cur[j] = res1 if len(res1) < len(res2) else res2
            prev = cur 
        
        return prev[0]