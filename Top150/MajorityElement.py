'''
169. Majority Element
Easy

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        value = len(nums)//2
        numsMap = {}
        for num in nums:
            if num in numsMap:
                numsMap[num] += 1
            else:
                numsMap[num] = 1

        for num, count in numsMap.items():
            if count > value:
                return num

        