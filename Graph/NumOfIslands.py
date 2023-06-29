'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 

You may assume all four edges of the grid are all surrounded by water.



Example:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
only 1 island is found.


'''

def num_of_islands(grid):
    
    #these next lines are usually base cases for graph qs
    
    if not grid or not grid[0]:
            return 0

    ROWS, COLS = len(grid), len(grid[0])
    visited = set()
    counter = 0

    def dfs(r,c):
        #make sure its inbound
        if (
            r not in range(ROWS) or
            c not in range(COLS) or
            grid[r][c] == "0" or
            (r,c) in visited
        ):
            return
        #b/c set use add
        visited.add((r,c))
        directions = [[0, 1], [0, -1], [1,0], [-1,0]]
        for dr, dc in directions:
            dfs(r + dr, c + dc)
        
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1" and (r,c) not in visited:
                counter += 1
                dfs(r,c)
    return counter
            
        
        