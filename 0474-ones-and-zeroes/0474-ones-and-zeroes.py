class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        table = defaultdict(int)
        for i,s in enumerate(strs) : 
            table[i] = Counter(s)
        # print(table)
        @cache
        def lss(i , m_cur , n_cur) : 
            if m_cur > m or n_cur > n  :
                return float('-inf')
            if i == len(strs) : 
                return 0
            leave = lss(i+1 , m_cur , n_cur)
            take =  1+lss(i+1 , m_cur+table[i]['0'] , n_cur+table[i]['1'])
            return max(take , leave) 
        return lss(0 , 0 , 0)