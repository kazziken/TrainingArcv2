'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

'''
import collections

def rottenOranges(self, grid):

    q = collections.deque()
    ROWS, COLS = len(grid), len(grid[0])

    fresh_oranges = 0
    time_til_rotten = 0

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                fresh_oranges += 1
            if grid[r][c] == 2:
                q.append((r,c))

    
    directions = [[0,1], [0, -1], [1,0], [-1,0]]

    while fresh_oranges > 0 and q is not None:
        for _ in range(len(q)):
            #pop the first one from the queue out
            r, c = q.popleft()
            
            # For each orange (r, c) in the queue, the loop checks its neighboring cells using the offsets from directions.
            for dr,dc in directions:
                row, col = r + dr, c + dc

                if (
                row in range(ROWS) and
                col in range(COLS) and 
                grid[r][c] == 1
                ):
                    grid[r][c] = 2
                    q.append((row, col))
                    fresh_oranges -= 1
        time_til_rotten += 1
    return time_til_rotten if fresh_oranges == 0 else - 1
