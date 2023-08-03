'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.


Input: m = 3, n = 7
Output: 28

'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #bottom row all 1's
        row = [1] * n

        #going through all rows exccept the last one
        for _ in range(m - 1):
            newRow = [1] * n
            #avoid edgecase of OOB
            for j in range(n - 2, -1, -1):
                #computing the newRow by going backwards and bottom row is all 1's.
                #value is the row after it (same row) and row beneath it(bottom row)
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]


'''Explanation:
We're operating in a bottom-up 2-D DP situation

Going from top left to bottom right, you have two situations at all times: go right or go down. Never left or up.

By that logic, The amount of operations on the bottom row is 1

Example

[[15][10][6][3][1]][0]
[[5][4][3][2][1]][0]
[[1][1][1][1][1]][0]

In this 3 x 5 grid, bottom must be all 1's. Going through each of the rows, for each elements within those rows, calculate the number of unique paths to reach the bottom-right cell.
The num of unique paths to reach a cell is equal to the sum of number of paths from the cell to it's right and the cell below it. B/c we can only move down or right.
The function then updates the newRow with this value
After processing all the cells in that current row, the 'row' list is updated with newRow.
We're constantly updating 'newRow' and 'row'. Eventually the answer is row[0] which is the top-left

The time complexity of this solution is O(m * n), and the space complexity is O(n) since we only store one row of the grid at a time.
'''