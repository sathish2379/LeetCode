'''
143. Reorder List
Medium

You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ############ Solution using StackQueue ############
        # stackQueue = []
        # temp = head
        # while temp.next != None:
        #     stackQueue.append(temp)
        #     temp = temp.next
        # stackQueue.append(temp)
        
        # head = stackQueue.pop(0)
        # temp = head
        # while stackQueue:
        #     temp.next = stackQueue.pop()
        #     temp.next.next = None
        #     if stackQueue:
        #         temp.next.next = stackQueue.pop(0)
        #         temp.next.next.next = None
        #     temp = temp.next.next

        def reverse(head):
            prev = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        def merge(l1, l2):
            merged = ListNode()
            i = 0
            curr = merged
            while l1 and l2:
                if i%2 == 0:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                i += 1
                curr = curr.next
            
            curr.next = l1 or l2
            return merged.next
        
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next
        slow.next = None
        l2 = reverse(l2)
        merge(head, l2)
        



        