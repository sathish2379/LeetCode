'''
19. Remove Nth node From End of List
Medium

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        # temp = head
        # count = 1
        # while temp:
        #     temp = temp.next
        #     count += 1
        # n_node = count - n

        # if n_node == 1:
        #     return head.next
        
        # temp = head
        # prev = None
        # while n_node>1:
        #     prev = temp
        #     temp = temp.next
        #     n_node -= 1
        # prev.next = temp.next
        # return head

        prev, curr, fast = None, head, head
        #moving fast to n offset
        for i in range(n):
            fast = fast.next

        while fast:
            prev = curr
            curr = curr.next
            fast = fast.next
        
        if prev:
            prev.next = curr.next
        else:
            head = head.next
        return head
        