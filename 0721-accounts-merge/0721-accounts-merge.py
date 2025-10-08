class UF : 
    def __init__(self , n) : 
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, n) : 
        p = self.par[n]
        while p != self.par[p] : 
            p = self.par[self.par[p]]
        return p
    def union(self, n1 , n2) : 
        p1 , p2 = self.find(n1) , self.find(n2)
        if p1 != p2 : 
            self.par[p1] = p2

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        
        email2index = {}

        for i,a in enumerate(accounts) : 
            for email in a[1:] : 
                if email in email2index : 
                    uf.union(i , email2index[email])
                else : 
                    email2index[email] = i

        emailGroup = defaultdict(list)
        for e , i in email2index.items() : 
            leader = uf.find(i)
            emailGroup[leader].append(e)

        res = []
        for i , email in emailGroup.items() : 
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        
        return res