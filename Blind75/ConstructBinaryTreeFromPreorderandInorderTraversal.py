'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium
** Important **

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # Find the root in the inorder segment to determine the left and right subtrees
            in_root_index = inorder_index[root_val]
            left_tree_size = in_root_index - in_start
            
            # Build the left and right subtrees
            root.left = build(pre_start + 1, pre_start + left_tree_size, in_start, in_root_index - 1)
            root.right = build(pre_start + left_tree_size + 1, pre_end, in_root_index + 1, in_end)
            
            return root
        
        # Create a map to get the index of each value in inorder traversal
        inorder_index = {value: index for index, value in enumerate(inorder)}
        
        # Call the build function with initial indices
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
        