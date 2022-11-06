from idlelib.tree import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def DFS(node, low, high):
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return DFS(node.right, node.val, high) and DFS(node.left, low, node.val)

        return DFS(root, float('-inf'), float('inf'))
"""

"""


