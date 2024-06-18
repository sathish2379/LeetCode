'''
76. Minimum Window Substring
Hard

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map_t = Counter(t)
        end, begin, head = 0, 0, 0
        tracker = len(t)
        d = float('inf')

        while end < len(s):
            if map_t[s[end]] > 0:
                tracker -= 1
            map_t[s[end]] -= 1
            end += 1

            while tracker == 0:
                if end - begin < d:
                    d = end - begin
                    head = begin
                map_t[s[begin]] += 1
                if map_t[s[begin]] > 0:
                    tracker += 1
                begin += 1
        return "" if d==float('inf') else s[head:head+d]
            
            
        