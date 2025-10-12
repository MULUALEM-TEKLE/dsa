class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ci = citations
        n = len(ci)
        counts = [0] * (n+1)

        for c in ci : 
            counts[min(n , c)] += 1 
        
        h = n 
        papers = counts[n]

        while papers < h : 
            h -= 1
            papers += counts[h]
        
        return h