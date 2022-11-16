"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。此外，你可以假设该网格的四条边均被水包围。
示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
"""
from typing import List


class Solution:
    def numofisland(self, grid: List[List[str]]):
        m = len(grid)
        n = len(grid[0])
        if not grid:
            return 0

        def dfs(grid, r, c):
            if not 0 <= r < m or not 0 <= c < n or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)

        island = 0
        for i in range(m):
            for j in range(n):
                ##当前元素为1，导语数量+1
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    island += 1
        return island

if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    print(Solution().numofisland(grid))
