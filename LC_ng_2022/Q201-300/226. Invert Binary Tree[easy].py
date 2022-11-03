# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode
from typing import Optional

"""
##DFS recusion
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        if root:
            right = self.invertTree(root.right)
            left = self.invertTree(root.left)

            root.left = right
            root.right = left

        return root
O(n)
O(n)
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        if root:
            right = self.invertTree(root.right)
            left = self.invertTree(root.left)

            root.left = right
            root.right = left

        return root
