'''
217. Contains Duplicate
Easy

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
     ############# Something Complex ###############
        seen = set()
        # nums.sort()
        # left = 0
        # right = len(nums) -1
        
        # while left < right:
        #     if nums[right] not in seen:
        #         seen.add(nums[right])
        #         right -= 1
        #         if right - 1 >= 0 and nums[right] == nums[right-1]:
        #             return True
        #     else:
        #         return True
        #     if nums[left] not in seen:
        #         seen.add(nums[left])
        #         left += 1
        #         if left + 1 < len(nums) and nums[left] == nums[left+1]:
        #             return True
        #     else:
        #         return True
            
            
                
        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                return True    
        return False
