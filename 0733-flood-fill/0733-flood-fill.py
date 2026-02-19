'''
-> mxn gird, where image[i][j] represents the pixel value of the image
-> given sr, sc , color 
    -> starting from images[sr][sc] change it from its original color to given color 
        -> gotta get ahold of the original color so we can identify its original color
        -> update neighbors/all other connected components so their color is updated if they are similar to the original pixel color
            -> do a dfs/bfs, find adjacent pixels with similar color and update them    
                -> I think bfs is better, lets explore it and get back
                -> gonna need a visited set so I dont visit again
                -> define directions [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]]

        -> logic flow
            -> get the original color 
            -> add it to a queue and visited set 
            -> update its color to new color and check neighbors and if they have similar original color add them to the queue
            -> loop until the queue is empty 

'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows , cols = len(image) , len(image[0])
        directions = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]]
        original_color = image[sr][sc]

        q = deque()
        visited = set()
        q.append((sr , sc))
        visited.add((sr , sc))
        image[sr][sc] = color

        while q : 
            for _ in range(len(q)) : 
                r , c = q.popleft()

                for dr , dc in directions : 
                    nr , nc = r+dr , c+dc

                    if nr in range(rows) and nc in range(cols) and (nr , nc) not in visited and image[nr][nc] == original_color : 
                        q.append((nr , nc))
                        visited.add((nr , nc))
                        image[nr][nc] = color 
        
        return image