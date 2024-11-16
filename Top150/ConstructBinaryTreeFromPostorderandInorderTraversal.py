'''
106. Construct Binary Tree from Inorder and Postorder Traversal
Medium

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def arrayToTree(in_left, in_right):
            if in_left > in_right:
                return None
            
            root_value = postorder.pop()
            root = TreeNode(root_value)

            root.right = arrayToTree(inorder_index_map[root_value] + 1, in_right)
            root.left = arrayToTree(in_left, inorder_index_map[root_value]-1)
            return root
        
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return arrayToTree(0, len(inorder)-1)
        