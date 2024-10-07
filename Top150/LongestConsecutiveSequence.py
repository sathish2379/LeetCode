'''
128. Longest Consecutive Sequence
Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        n = len(nums)
        nums_set = set(nums)
        maxLength = 1
        for num in nums_set:
            if num-1 not in nums_set:
                length = 1
                start = num
                while start+1 in nums_set:
                    length += 1
                    start += 1
                maxLength = max(maxLength, length)
        return maxLength