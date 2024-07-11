'''
49. Group Anagrams
Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
 
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for string in strs:
            sorted_chars = sorted(string)
            sorted_string = ''.join(sorted_chars)
            if sorted_string in hashMap:
                hashMap[sorted_string].append(string)
            else:
                hashMap[sorted_string] = [string]
        return list(hashMap.values())
