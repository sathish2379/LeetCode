'''
238. Product of Array Except Self
Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n
        ########### Solution using two variables ##########
        # prefix = 1
        # suffix = 1
        # for i in range(n):
        #     if i==0:
        #         answer[i] = 1
        #     else:
        #         prefix = prefix*nums[i-1]
        #         answer[i] = prefix
            
        # for i in range(n):
        #     j = n-i-1
        #     if j == n-1:
        #         answer[j] = answer[j]*1
        #     else:
        #         suffix = suffix*nums[j+1]
        #         answer[j] = answer[j]*suffix

        ############## Solution without using extra space ############
        for i in range(1, n):
            answer[i] = answer[i-1]*nums[i-1] 

        for j in range(n-2, -1, -1):
            answer[j] = answer[j]*nums[j+1]
            nums[j] = nums[j]*nums[j+1]

        return answer


        