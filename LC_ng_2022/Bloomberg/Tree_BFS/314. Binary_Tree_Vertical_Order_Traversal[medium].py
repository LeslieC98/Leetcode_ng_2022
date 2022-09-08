# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode
from typing import Optional, List
from collections import deque, defaultdict


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        # the col->nodes.val[] map
        columns = defaultdict(list)

        # BFS
        queue = deque([(root, 0)])
        while len(queue) > 0:
            node, col = queue.popleft()
            columns[col].append(node.val)
            if node.left: queue.append((node.left, col - 1))
            if node.right: queue.append((node.right, col + 1))

        # columns is now a list of tuples (col, nodes.val[])
        columns = sorted(columns.items())
        res = []
        for col in columns:
            res.append(col[1])
        return res
