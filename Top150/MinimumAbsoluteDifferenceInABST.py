'''
530. Minimum absolute difference in BST
Easy

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sorted_order=[]
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def _inorder(root):
            if root is None:
                return

            _inorder(root.left)
            self.sorted_order.append(root.val)
            _inorder(root.right)

        _inorder(root)
        minimum = float("inf")

        for i in range(0, len(self.sorted_order)-1):
            diff = abs(self.sorted_order[i+1] - self.sorted_order[i])
            if diff < minimum:
                minimum = diff
        return minimum

         

        return 0
            

        