'''
2. Add two numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        a = l1
        b = l2
        c = ListNode()
        result = c
        # while a and b:
        #     result.val = carry + a.val + b.val
        #     carry = result.val//10
        #     result.val = result.val % 10
        #     a = a.next
        #     b = b.next
        #     if a or b or carry > 0:
        #         result.next = ListNode()
        #         result = result.next
        # while a:
        #     result.val = carry + a.val
        #     carry = result.val//10
        #     result.val = result.val % 10
        #     a = a.next
        #     if a or carry > 0:
        #         result.next = ListNode()
        #         result = result.next
        
        # while b:
        #     result.val = carry + b.val
        #     carry = result.val//10
        #     result.val = result.val % 10
        #     b = b.next
        #     if b or carry > 0:
        #         result.next = ListNode()
        #         result = result.next

        # if carry > 0:
        #     result.val = carry

        # return c

        # Another Solution avoiding redundant code
        dummy = ListNode()
        curr = dummy 
        carry = 0
        while l1 or l2 or carry:
            one = l1.val if l1 else 0
            two = l2.val if l2 else 0 
            total = (one + two + carry) 
            curr.next = ListNode(total%10)
            carry = total // 10
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next


                     