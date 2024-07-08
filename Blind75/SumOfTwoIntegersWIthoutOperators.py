'''
371. Sum of Two Integers**
Medium

Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5
'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        MIN = 0x80000000
        MASK = 0xFFFFFFFF
        
        while b != 0:
            # Calculate carry
            carry = (a & b) & MASK
            
            # Sum without carry
            a = (a ^ b) & MASK
            
            # Shift carry left
            b = (carry << 1) & MASK
        
        # Handle negative numbers using mask
        return a if a <= MAX else ~(a ^ MASK)
        