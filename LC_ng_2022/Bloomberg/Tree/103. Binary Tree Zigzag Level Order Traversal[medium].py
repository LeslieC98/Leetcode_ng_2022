import collections
from idlelib.tree import TreeNode
from typing import Optional, List



class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        flag = 1
        res = []
        while len(queue) != 0:
             ### 声明stack
            level= []
            for i in range(len(queue)):
                ##取出node节点
                node = queue.popleft()
                ##把取出的节点的值放入level中
                level.append(node.val)
                 # 将下一层的节点存放到 queue 中
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 偶数层，将level直接插入
            if flag == 1:
                res.append(level[:])
                flag = 0
             # 奇数层，将level 反转
            else:
                res.append(level[::-1])
                flag = 1
        return res
