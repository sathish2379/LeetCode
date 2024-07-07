'''
152. Maximum Product Subarray
Medium

Given an integer array nums, find a 
subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            temp_max = max_product
            max_product = max(nums[i], nums[i]*temp_max, nums[i]*min_product)
            min_product = min(nums[i], nums[i]*temp_max, nums[i]*min_product)
            global_max = max(global_max, max_product)
        return global_max