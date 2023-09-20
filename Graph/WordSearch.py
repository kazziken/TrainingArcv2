def exists(word, matrix):

    rows, cols = len(matrix), len(matrix[0])

    visited = set()

    #helper func
    def dfs(r, c, i):

        if i == len(word):
            return True

        if (r < 0 or
            c < 0 or
            r >= rows or
            c >= cols or
            word[i] != matrix[r][c] or
            (r,c) in visited
            ):
            return False
        
        visited.add((r,c))
        res = (dfs(r + 1, c, i + 1) or
               dfs(r - 1, c, i + 1) or
               dfs(r, c + 1, i + 1) or
               dfs(r, c - 1, i + 1) 
               )
        visited.remove((r,c))
        return res
    
    for row in range(rows):
        for col in range(cols):
            if dfs(row, col, 0): return True
    return False
