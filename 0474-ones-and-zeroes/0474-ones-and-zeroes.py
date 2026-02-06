class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        table = defaultdict(int)

        for i , s in enumerate(strs) : 
            table[i] = Counter(s)
        
        @cache
        def lss(i, n_c , m_c) : 
            if n_c > n or m_c > m : 
                return -1
            if i == len(strs) : 
                return 0
            return max(lss(i+1 , n_c , m_c) , 1 + lss(i+1 , n_c+strs[i].count('1') , m_c+strs[i].count('0')))
        
        return lss(0 , 0, 0)