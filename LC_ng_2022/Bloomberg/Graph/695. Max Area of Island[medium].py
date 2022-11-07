from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = grid
        n = grid[0]

        def dfs(grid, r, c):
            ##The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function. Use the keyword nonlocal to declare that the variable is not local.
            nonlocal size
            if not 0 <= r < len(m) or not 0 <= c < len(n):
                return
            if grid[r][c] != 1:
                return
            grid[r][c] = 0  ##when we has been visited,relabel as 0
            size += 1  # 有一个陆地格子，面积size就+1
            dfs(grid, r - 1, c)
            dfs(grid, r + 1, c)
            dfs(grid, r, c - 1)
            dfs(grid, r, c + 1)

        res = 0
        for r in range(len(m)):
            for c in range(len(n)):
                size = 0  # 初试化面积size
                if grid[r][c] == 1:
                    dfs(grid, r, c)
                    res = max(res, size)
        return res


##time O(n)
##space O(n)