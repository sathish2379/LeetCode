'''
28. Find the Index of first occurence in a string
Easy

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle) - simple solution

        if not needle:
            return 0

        needle_length = len(needle)
        haystack_length = len(haystack)

        for i in range(haystack_length - needle_length + 1):
            if haystack[i:i + needle_length] == needle:
                return i

        return -1  