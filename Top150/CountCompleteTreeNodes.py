'''
222. Count Complete Tree Nodes
Easy

Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
Design an algorithm that runs in less than O(n) time complexity.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [1]
Output: 1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # simple solution is traverse the tree and count nodes
        return 1+self.countNodes(root.right)+self.countNodes(root.left) if root else 0

        # Time complexity : O(N).
        # Space complexity : O(d)=O(logN) to keep
        # the recursion stack, where d is a tree depth.

        #This approach doesn't profit from the fact that tree is complete one.
        # That means that complete tree has 2^k nodes in the kth level
        # The last level may be not filled completely,
        # and hence in the last level the number of nodes   
        # could vary from 1 to 2^d, where d is a tree depth
        
        # But this approach is difficult to understand
        # Review it later
        