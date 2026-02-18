class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        server_locations = []
        total_server_counts = 0
        for r in range(rows) : 
            for c in range(cols) : 
                if grid[r][c] == 1 : 
                    server_locations.append((r , c))
                    total_server_counts += 1 
        
        # print(server_locations)
        
        for r , c in server_locations : 
            neighbor_found = False
            # check row 
            for i in range(rows) : 
                if (i , c) != (r , c) and grid[i][c] == 1 :
                    # print(f"neighbor found at grid[{i}][{c}]")
                    neighbor_found = True 
                    
            # check col
            for i in range(cols) : 
                if (r , i) != (r , c) and grid[r][i] == 1 :
                    # print(f"neighbor found at grid[{r}][{i}]")
                    neighbor_found = True 
                    
            # print(f"neighbor found {neighbor_found}")
            if neighbor_found == False : total_server_counts -= 1 

        return total_server_counts
            
            # if nothing is found decrement from total count
            

