import collections
from idlelib.tree import TreeNode
from typing import Optional, List

import null as null

import collections


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = collections.deque([root])
        res = []
        while queue:
            res.append([node.val for node in queue])
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
if __name__ == '__main__':
    root = [3,9,20,null,null,15,7]
    print(Solution().levelOrder(root))