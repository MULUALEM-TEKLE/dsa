class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = defaultdict(list)

        for u,v in edges : 
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        
        def explore(node) : 
            if node == destination : 
                return True 
            
            visited.add(node)
            for neighbor in adj[node] : 
                if neighbor not in visited : 
                    if explore(neighbor) : return True
            return False

        return explore(source)
