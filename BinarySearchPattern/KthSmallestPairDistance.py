'''
719. Find K-th Smallest Pair Distance
Hard

The distance of a pair of integers a and b is defined as the absolute difference between a and b.
Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

Example 1:
Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.

Example 2:
Input: nums = [1,1,1], k = 2
Output: 0

Example 3:
Input: nums = [1,6,1], k = 3
Output: 5
'''

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        def countPairs(distance: int) -> bool:
            count, i, j = 0, 0, 0
            while i<n or j<n:
                while j<n and nums[j] - nums[i] <= distance:
                    j+=1
                count += j-i-1
                i += 1
            return count >= k

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left)//2
            if countPairs(mid):
                right = mid
            else:
                left = mid+1
        return left
         