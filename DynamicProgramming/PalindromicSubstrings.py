'''
647. Palindromic Substrings
Medium

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        count = 0

        for i in range(n):
            dp[i][i] = True
            count+=1

        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count+=1

        for l in range(3, n+1):
            for i in range(0, n-l+1):
                j = i+l-1
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    count+=1
                else:
                    dp[i][j]=False
                
        return count