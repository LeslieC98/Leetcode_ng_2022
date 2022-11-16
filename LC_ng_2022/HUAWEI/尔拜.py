from typing import List

## DFS time:O(M*N) space: O(M*N)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        if not grid:
            return 0
        ##定义一个函数，用于深度优先搜索，将当前位置的相邻位置全部标记为0
        def dfs(grid, r, c):
            # 如果当前位置超出网格的范围，则返回，如果当前位置为0，则表示已经访问过，则返回
            if not 0 <= r < m or not 0 <= c < n or grid[r][c] == "0":
            # 将当前位置标记为0，表示已经访问过
            grid[r][c] = "0"
            递归调用dfs函数，将当前位置的上下左右位置全部标记为0
            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)

        island = 0 #定义一个变量，用于记录岛屿的数量
        for r in range(m): ##遍历网格中的每一个元素
            for c in range(n):
                # 如果当前元素为1，则表示该位置为陆地，岛屿数量加1
                if grid[r][c] == "1":
                    # 调用dfs函数，将当前位置的相邻位置全部标记为0，表示已经访问过
                    dfs(grid, r, c)
                    island += 1
        return island ##返回岛屿的数量
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


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(Solution().numIslands(grid))