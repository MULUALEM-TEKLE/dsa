'''
-> row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

-> One cell is a square with side length 1
    -> if only one sell perimeter = 4
-> Grid cells are connected horizontally/vertically (not diagonally).
    -> directions = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]]
        -> bfs?? 
            -> if the next cell is out of boundary or water, then increase the perimeter by 1. means this part is exposed
        -> dfs??
            -> we can also implement using bfs
-> The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
    -> only one island, not have to worry about multiple islands
-> Determine the perimeter of the island.
    -> perimeter is the addition of the sides of the edges of the island
    -> determining area is simple, is there any relationship?
    -> also gotta know the ones on the edge of the island, the center ones doesnt matter  

    implementation
        -> simple version, 
        -> for each cell, if its 1 check if its neighbor is out of bound or is water, if so add 1, else do nothing 
        -> accumulate each cell's result into a bigger result 
        -> return result


'''
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        directions = [[0 , 1] , [0 , -1] , [1 , 0] , [-1 , 0]]
        def check_neighbors(r , c) : 
            perimeter = 0
            for dr , dc in directions :
                nr , nc = r+dr , c+dc 
                if nr not in range(rows) or nc not in range(cols) or grid[nr][nc] == 0 :
                    perimeter += 1 
            return perimeter 
        
        res = 0 

        for r in range(rows) : 
            for c in range(cols) : 
                if grid[r][c] == 1 : 
                    res += check_neighbors(r , c)
        
        return res 