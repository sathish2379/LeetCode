'''
242. Valid Anagram
Easy

Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_s = {}
        hash_t = {}
        for i in range(0, len(s)):
            if s[i] in hash_s:
                hash_s[s[i]] += 1
            else:
                hash_s[s[i]] = 1

            if t[i] in hash_t:
                hash_t[t[i]] += 1
            else:
                hash_t[t[i]] = 1
        # sorted_s = {key: hash_s[key] for key in sorted(hash_s)}
        # sorted_t = {key: hash_t[key] for key in sorted(hash_t)}
        # if sorted_s == sorted_t:
        #     return True
        ########### Sorting is not necessary to compare hash tables ################
        if hash_s == hash_t:
            return True
        return False

        ############ we can simply use collections.counter for counting hashable elements in a string #########
        