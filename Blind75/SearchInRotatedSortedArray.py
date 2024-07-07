'''
33. Search in Rotated Sorted Array
Medium

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1 
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(start, end):
            while start <= end:
                mid = (start + end)//2
                print(mid)
                if nums[mid] < target:
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    return mid
            return -1

        left = 0
        right = len(nums) - 1
        while True:
            if nums[left]<=nums[right]:
                break
            left+=1
        start = 0
        end = left - 1
        right = len(nums) - 1

        first_sol = binarySearch(start, end)
        if first_sol == -1:
            return binarySearch(left, right)
        else: 
            return first_sol


    ######################### Another Approach ##################
    #  l,r= 0, len(nums)-1
    #     while(l<=r):
    #         m= l+(r-l)//2
    #         if target== nums[m]:
    #             return m
    #         if nums[l]<=nums[m]:
    #             if target<nums[l] or target>nums[m]:
    #                 l= m+1
    #             else:
    #                 r= m-1
    #         else:
    #             if target>nums[r] or target< nums[m]:
    #                 r= m-1
    #             else:
    #                 l= m+1
            


        