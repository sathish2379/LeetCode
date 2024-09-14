'''
88. Merge Sorted Array
Easy

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # This is a regular solution, also we are actually not modifying nums1 in-place.
        # arr = [0]*(m+n)
        # i=0
        # j=0
        # k=0
        # while i < m and j < n:
        #     if(nums1[i] < nums2[j]):
        #         arr[k] = nums1[i]
        #         i+=1
        #     else:
        #         arr[k] = nums2[j]
        #         j+=1
        #     k+=1
        
        # while i<m:
        #     arr[k] = nums1[i]
        #     i+=1
        #     k+=1

        # while j<n:
        #     arr[k] = nums2[j]
        #     j+=1
        #     k+=1 

        # i=0
        # while i < (m+n):
        #     nums1[i] = arr[i]
        #     i+=1

        #The other solution is to start from the last element/greatest element. Since we have
        # 0's in nums1 which is of size m+n. we can start filling the positions.  
        # We will continue doing this until we have iterated through all the elements in nums2. If there are still elements left in nums1, we don't need to do anything because they are already in their correct place.
        #Thus the arrays can be merged and stay sorted

        i = m-1
        j = n-1
        k = m+n-1

        while j>=0:
            if i>=0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1

            

        