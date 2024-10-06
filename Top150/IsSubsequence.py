'''
392. IsSubsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        prev_index = 0
        count = 0
        if s == "":
            return True
        elif s == "" and t == "":
            return True
        
        for ch in s:
            for i in range(prev_index, len(t)):
                if ch == t[i]:
                    prev_index = i+1
                    count += 1
                    break

        if count == len(s):
            return True
        return False

        #### Two pointer solution ####
        # left is pointer for s
        # right is point for t

        # left = 0
        # right = 0
        # left_bound = len(s)
        # right_bound = len(t)
        
        # while left < left_bound and right < right_bound:
        #     if s[left] == t[right]:
        #         left +=1
        #     right += 1

        # # left is doing the job of count as well.
        # return left == left_bound
        