'''
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        if s is None:
            return True
            
        stack = []
        for c in s:
            if c is '(' or c is '[' or c is '{':
                stack.append(c)
            if stack:
                if c is ')':
                    if stack[-1] is not '(':
                        return False
                    else:
                        stack.pop()
                elif c is ']':
                    if stack[-1] is not '[':
                        return False
                    else:
                        stack.pop()
                elif c is '}':
                    if stack[-1] is not '{':
                        return False
                    else:
                        stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
        
        