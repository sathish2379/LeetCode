'''
200. Number of Islands
Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(grid, x, y):
            # Checking if (x, y) is out of bounds or not land ('0')
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '0':
                return
            grid[x][y] = '0'
            dfs(grid, x, y - 1) 
            dfs(grid, x + 1, y)  
            dfs(grid, x - 1, y)  
            dfs(grid, x, y + 1)  
        
        counter = 0
        m , n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':  
                    counter += 1  
                    dfs(grid, i, j)  

        return counter

        