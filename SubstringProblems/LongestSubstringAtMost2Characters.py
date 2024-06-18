'''
159. Longest Substring with At Most Two Distinct Characters
Hard

Given a string s, find the length of the longest substring t that contains at most 2 distinct characters.

Example 1:
Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.

Example 2:
Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
'''
def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    if not s:
        return 0
    
    map = [0] * 128 
    counter, begin, end = 0, 0, 0
    d = 0

    while end < len(s):
        if map[ord(s[end])] == 0:
            counter += 1
        map[ord(s[end])] += 1
        end += 1

        while counter > 2:
            if map[ord(s[begin])] == 1:
                counter -= 1
            map[ord(s[begin])] -= 1
            begin += 1
        if end - begin > d:
            d = end - begin
    return d

s = "eceaae"
print(lengthOfLongestSubstringTwoDistinct(s))

