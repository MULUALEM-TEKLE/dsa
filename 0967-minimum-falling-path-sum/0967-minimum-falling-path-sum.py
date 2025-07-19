'''
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
-> square
-> falling defined below

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. 
-> start from first row, fall down to left,right,below in bound till you get to the bottom row
-> caching??? --> will decide later
-> base case got to the bottom row , return its grid value
-> base case, got out of bounds, return infinity since we are looking for a min value here
-> recursive case :
    -> explore the possible cells and find min and add it to the cell value
    -> min(dfs(r+1 , c-1) , dfs(r+1 , c) , dfs(r+1 , c+1)) + grid[r][c]
-> we also have to find the minmum of all the first row elements : 
    -> for c in range(cols) : find and return the minimum(dfs(0 ,c))


Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

'''

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = cols = len(matrix)
        res = float('inf')

        memo = {}
        def dfs(r , c) : 
            if (r , c) in memo : return memo[(r , c)]
            if r not in range(rows) or c not in range(cols) : return float('inf')
            if r == rows-1 : 
                return matrix[r][c]
            
            memo[(r , c)] = min(dfs(r+1 , c-1) , dfs(r+1 , c) , dfs(r+1 , c+1)) + matrix[r][c]
            return memo[(r , c)]
        
        for c in range(cols) : 
            res = min(res , dfs(0 , c))
        
        return res
