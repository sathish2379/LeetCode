'''
130. Surrounded Regions
Medium

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation:
In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:
Input: board = [["X"]]
Output: [["X"]]
'''


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m, n = len(board), len(board[0])
        def dfs(x, y):
             # Checking if (x, y) is out of bounds or not region ('X')
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != 'O':
                return
            
            board[x][y] = '#'
            dfs(x, y+1)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x-1, y)


        # Step 1: Mark all 'O's connected to the boundary
        for i in range(m):
            if board[i][0] == 'O': # Left boundary
                dfs(i, 0)
            if board[i][n - 1] == 'O':  # Right boundary
                dfs(i, n - 1)

        for j in range(n):
            if board[0][j] == 'O': # Top boundary
                dfs( 0, j)
            
            if board[m-1][j] == 'O': # Bottom boundary
                dfs( m-1, j)

        # Step 2:  Convert all remaining 'O's to 'X' and '#' back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'