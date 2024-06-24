'''
110. Balanced Binary Tree
Easy

Given a binary tree, determine if it is 
height-balanced.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.heightTree(root) != -1
        # if root is None:
        #     return True

        # leftHeight = self.height(root.left)
        # rightHeight = self.height(root.right)
        # return abs(rightHeight - leftHeight )<=1 and self.isBalanced(root.right) and self.isBalanced(root.left) 

    
    def height(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1

    def heightTree(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        
        left = self.heightTree(node.left)
        right = self.heightTree(node.right) 
        print(left)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
