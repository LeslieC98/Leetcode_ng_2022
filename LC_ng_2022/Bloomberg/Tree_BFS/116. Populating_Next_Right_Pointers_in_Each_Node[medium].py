"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

import collections
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return []
        queue = collections.queue([root])
        while queue:

            for i in range(len(queue)):
                node = queue.popleft()
                ##如果它不是该层的最后一个元素，那么把它指向队列中的后面的元素（不把后面的这个弹出）
                if i < len(queue) -1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
"""
We traversal all nodes of the tree once so the time complexity is O(n)
space: o(n)
We're simulating BFS with a queue, so the queue is going to go through the tree, so it's order N.
"""