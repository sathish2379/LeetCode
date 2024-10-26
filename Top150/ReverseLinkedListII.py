'''
92. Reverse Linked List II
Medium

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        a = head
        count = 1
        prev_node = None
        while count < left:
            prev_node = a
            a = a.next
            count +=1

        count = right - left + 1
        left_node = a
        prev = None
        next_node = None
        while count > 0 and a:
            next_node = a.next      
            a.next = prev      
            prev = a
            a = next_node
            count -=1 

        if left_node:
            left_node.next = next_node 

        if prev_node:
            prev_node.next = prev
        else:
            return prev

        return head

        
