class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parent = {}
        self.rank = {}

        for i in range(1 , len(edges)+1) : 
            self.parent[i] = i
            self.rank[i] = 0
        
        def find(n) : 
            p = self.parent[n]

            while p != self.parent[p] : 
                self.parent[p] = self.parent[self.parent[p]]
                p = self.parent[p]
            return p
        
        def union(n1 , n2) : 
            p1 , p2 = find(n1) , find(n2)
            if p1 == p2 : return False 

            if self.rank[p1] > self.rank[p2] : 
                self.parent[p2] = p1
            elif self.rank[p2] > self.rank[p1] : 
                self.parent[p1] = p2
            else : 
                self.parent[p2] = p1
                self.rank[p1] += 1 
            return True
        

        for n1,n2 in edges : 
            if not union(n1 , n2) : 
                return [n1, n2]
        


