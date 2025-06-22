class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def in_bound(x, y):
            return 0 <= x < len(board) and 0 <= y < len(board[0]) 
    
        def direction(x, y):
            neighbors = []
            for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if in_bound(x + i, y + j):
                    neighbors.append((x + i, y + j))
            return neighbors
        
        # Check for each starting positions
        def dfs_check(curr, i, j, visited):
            visited.add((i, j))
            if curr + 1 == len(word):
                return True
            for x, y in direction(i, j): 
                if board[x][y] == word[curr + 1] and (x, y) not in visited:
                    visited.add((x, y))
                    if dfs_check(curr + 1, x, y, visited):
                        return True
            visited.remove((i, j))
            return False

        # collect word freq.
        locations = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board[0])):
                locations[board[i][j]].append([i, j])

        # run dfs check
        for i, j in locations[word[0]]:
            if dfs_check(0, i, j, set()):
                return True
        return False