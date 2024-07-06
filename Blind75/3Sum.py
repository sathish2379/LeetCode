'''
15. 3 Sum
Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        seen = set()
        ########## BRUTE FORCE #############
        # for k in range(n):
        #     sum_ = -nums[k]
        #     for i in range(0,n):
        #         if i==k:
        #             continue
        #         for j in range(i+1, n):
        #             if j==k:
        #                 continue
        #             if nums[i] + nums[j] == sum_:
        #                 j = nums.index(sum_ - nums[i])
        #                 tripletList = sorted([nums[i], nums[j], nums[k]])
        #                 triplet = tuple(tripletList)
        #                 if triplet not in seen:
        #                     seen.add(triplet)
        #                     result.append(list(triplet))

        nums.sort()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1
            while left < right:
                total = nums[left] + nums[i] + nums[right]
                if total < 0:
                    left +=1
                elif total > 0:
                    right -= 1
                else:
                    triplet = (nums[i], nums[left], nums[right])
                    if triplet not in seen:
                        seen.add(triplet)
                        result.append([nums[left], nums[i], nums[right]])
                    left += 1
                    right -= 1
                    while left + 1 < right and nums[left] == nums[left-1]:
                        left+=1
        return result