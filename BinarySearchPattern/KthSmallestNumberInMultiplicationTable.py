'''
668. Kth Smallest Number in Multiplication Table
Hard

Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).
Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.

Example 1:
Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The 5th smallest number is 3.

Example 2:
Input: m = 2, n = 3, k = 6
Output: 6
Explanation: The 6th smallest number is 6.
'''

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def isKNumbersAvailable(num: int) -> bool:
            count = 0
            for val in range(1, m+1):
                count+=min(num//val, n)
            return count >= k

        left, right = 1, m*n
        while left < right:
            mid = left + (right - left)//2
            if isKNumbersAvailable(mid):
                right = mid
            else:
                left = mid + 1
        return left

        