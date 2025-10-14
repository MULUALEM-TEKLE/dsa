from heapq import heappop , heappush
class UF : 
    def __init__(self , n) : 
        self.par = [i for i in range(n)]
    
    def find(self , n) : 
        p = self.par[n]
        while p != self.par[p] : 
            p = self.par[self.par[p]]
        return p
    def union(self, n1 , n2) : 
        p1 , p2 = self.find(n1) , self.find(n2)
        if p1 == p2 : 
            return False 
        self.par[p1] = p2
        return True

        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # adj = defaultdict(list)
        adj = []
        points = [tuple(point) for point in points]

       
        for i in range(len(points)) : 
            x1 , y1 = points[i]
            for j in range(i+ 1 , len(points)) : 
                x2 , y2 = points[j]

                cost = abs(x1-x2) + abs(y1-y2)

                adj.append([i , j , cost])
                adj.append([j , i , cost])

                # adj[(x1 , y1)].append([(x2 , y2) , cost])
                # adj[(x2 , y2)].append([ (x1 , y1), cost])
        
        # print(adj)
        
        # pq = []
        # for neighbor, cost in adj[points[0]] : 
        #     heappush(pq , [cost , neighbor])

        # total_cost = 0
        # visited = set()
        # visited.add(points[0])

        # while pq : 
        #     cost , node = heappop(pq)
        #     if node in visited : 
        #         continue
        #     visited.add(node)
        #     total_cost += cost 
        #     for neighbor , cost in adj[node] : 
        #         if neighbor not in visited :
        #             heappush(pq , [cost , neighbor])
        
        # return total_cost

        n = len(points)
        uf = UF(n)
        pq = []
        for src , dst , cost in adj : 
            heappush(pq , [cost , src , dst])
        
        mst = []
        res = 0
        while len(mst) < n-1 : 
            cost , src , dst = heappop(pq)
            if not uf.union(src , dst) : 
                continue 
            mst.append([src , dst])
            res += cost
        return res
