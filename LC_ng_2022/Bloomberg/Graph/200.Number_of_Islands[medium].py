from typing import List

## DFS time:O(M*N) space: O(M*N)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(grid, r, c):
            if not 0 <= r < m or not 0 <= c < n or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)

        island = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(grid, r, c)
                    island += 1
        return island
"""
##BFS solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        m = len(grid)
        n = len(grid[0])

        def bfs(i, j):

            queue = [[i, j]]
            queue.append((i, j))
            grid[i][j] = "0"

            while queue:
                (i, j) = queue.pop(0)
                ## 注意这里不可以grid[x][y] = "#" 因为

                for (x, y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == "1":
                        queue.append((x, y))
                        grid[x][y] = "0"  ##把append 视为遍历了这个元素 否则可能会造成重复遍历元素的困境

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i, j)
                    island += 1

        return island