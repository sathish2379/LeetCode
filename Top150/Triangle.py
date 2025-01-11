'''
120. Triangle
Medium

Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m=len(triangle)
        prev= triangle[m-1][:]
        cur =[0] * len(triangle[-1])
        for i in range(m-2,-1,-1):            
            for j in range(i,-1,-1):
                down=triangle[i][j] + prev[j]
                diag=triangle[i][j] + prev[j+1]
                cur[j]=min(down,diag)
            prev=cur[:]
        return prev[0]
        