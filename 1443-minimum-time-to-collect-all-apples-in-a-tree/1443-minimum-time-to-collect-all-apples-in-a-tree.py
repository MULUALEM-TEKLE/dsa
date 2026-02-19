'''
n vertices 0 to n-1 , some have apples and others dont
edges = [a , b] a->b 
    -> gotta build a graph using this data
    -> dfs?? 
        -> do a dfs on each subtree and use that time to accumulate
        -> keep track of the parent so we dont revisit
        -> if a subtree has an apple down the tree or if itself has an apple add to time 
edge walk takes 1 sec 
    -> will be tolling time for every walk and back which will be 2
find min time to collect all apples, starting at v=0 and coming back (the *2 comes into play here)
hasApple[i] boolean array indicating presence of apple
    -> some kind of check is going to be needed here to minimize time or decide if apple is present

print(f"adding time { (level+1) * 2  } on level {level+1} for node {child}")
'''
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # construct a graph
        tree = defaultdict(list)

        for src , dst in edges : 
            tree[src].append(dst)
            tree[dst].append(src)
        
        def dfs(cur , visited) : 
            time = 0 

            visited.add(cur)

            for neighbor in tree[cur] : 
                if neighbor in visited : 
                    continue
                neighbor_time = dfs(neighbor , visited)

                if neighbor_time or hasApple[neighbor] : 
                    time += neighbor_time + 2 
            
            return time 
        
        return dfs(0 , set())

            
                        
