'''
219. Contains Duplicate II
Easy

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexmap = {}
        for i in range(0, len(nums)):
            if nums[i] in indexmap:
                if abs(i - indexmap[nums[i]]) <= k:
                    return True
                else:
                    indexmap[nums[i]] = i
            else:
                indexmap[nums[i]] = i
        return False
        