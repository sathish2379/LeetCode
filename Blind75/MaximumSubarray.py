'''
53. Maximum Subarray
Medium

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        max_sum = float('-inf')
        current_sum = 0
        left = 0
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            if current_sum > max_sum:
                max_sum = current_sum

            #### To make sure that the next sum is not decreased, if the current_sum is negative. ###
            if current_sum < 0:
                current_sum = 0
                left = right + 1
        return max_sum

        #### Need to learn another approach using Divide and Conquer
        