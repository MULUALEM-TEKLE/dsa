class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lres = [1]*n
        cres = [1]*n
        @cache 
        def dp(i) : 
            lis = 1 
            count = 1 
            for j in range(i) : 
                if nums[j] < nums[i] : 
                    plis , pcount = dp(j)
                    clin = 1+plis
                    if clin > lis : 
                        lis = clin 
                        count = pcount
                    elif clin == lis : 
                        count += pcount
            lres[i] = lis
            cres[i] = count
            return (lis, count)
        
        for i in range(n) : 
            dp(i)
        
        output = 0
        
        maxl = max(lres)
        for i in range(n) : 
            if lres[i] == maxl : output += cres[i]
        
        return output
        
        
        