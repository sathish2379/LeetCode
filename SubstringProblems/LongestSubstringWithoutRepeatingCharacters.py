'''
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: #Complexity O(N)
        char_index_map = {}
        max_length = 0
        start = 0
        for index in range(len(s)):
            if s[index] in char_index_map and char_index_map[s[index]] >= start:
                start = char_index_map[s[index]] + 1
            char_index_map[s[index]] = index
            max_length = max(max_length, index - start + 1)
        return max_length

    def lengthOfLongestSubstring_(self, s: str) -> int: #higher complexity
        map = [0]*128
        counter, end, begin, d = 0, 0, 0, 0

        while end < len(s):
            if map[ord(s[end])] > 0:
                counter += 1
            map[ord(s[end])] += 1
            end+=1

            while counter > 0:
                if map[ord(s[begin])] > 1:
                    counter -= 1
                map[ord(s[begin])] -= 1
                begin += 1
            d = max(d, end - begin)
        return d 
