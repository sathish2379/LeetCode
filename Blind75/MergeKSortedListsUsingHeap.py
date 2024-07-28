'''
23. Merge K Sorted lists
Hard
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
'''

from heapq import heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#     def __lt__(self, other): # If this would have worked we wouldn't have to add elements into the tuple in heappush.
#         return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        # return self.mergeK(lists, 0, len(lists)-1)

        heap = []
        for i, l in enumerate(lists):
            if l:
                heappush(heap, (l.val, i, l)) #initializing heap with the head of each list
                # we have added l.val and i to we avoid the issue of Python trying to compare ListNode objects directly. 
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            val, i, smallest = heappop(heap)
            current.next = smallest
            current = current.next

            if smallest.next:
                heappush(heap, (smallest.next.val, i, smallest.next))
        
        return dummy.next


    def mergeK(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = (left+right)//2
        l1 = self.mergeK(lists, left, mid)
        l2 = self.mergeK(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 if l1 else l2
        return dummy.next
        