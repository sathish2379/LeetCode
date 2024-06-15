'''
62. Unique Paths
Medium

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        columns = n
        grid = [[0]*n for _ in range(0,m)]
        grid[0][0] = 1
        
        if n > 1:
            grid[0][1] = 1

        if m > 1:
            grid[1][0] = 1

        for i in range(2, m):
            grid[i][0] = grid[i-1][0]
        for j in range(2,n):
            grid[0][j] = grid[0][j-1] 


        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = (grid[i-1][j] + grid[i][j-1])

        return grid[-1][-1]