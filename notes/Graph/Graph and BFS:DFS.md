# 1. 图的定义

![image-20220909211252623](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220909211252623.png)

![image-20220909211453535](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220909211453535.png)

![image-20220909211825206](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220909211825206.png)



# 2. 岛屿问题

**深度优先遍历DFS和广度优先遍历BFS**

DFS和BFS均为树/图的搜索方式，能够访问树/图中的所有节点。

**DFS：**优先移动节点，当对给定节点尝试过每一种可能性之后，才退到前一节点来尝试下一个位置。**就像一个搜索者尽可能地深入调查未知的地域，直到遇到死胡同才回头。**

**BFS：**优先对给定节点的下一个位置进行尝试，当对给定节点尝试过每一种可能性之后，才移动到下一个节点。**就像一只搜索军队铺展开来覆盖领土，直到覆盖了所有地域。**

![image-20220910113623091](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220910113623091.png)



![image-20220910113746832](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220910113746832.png)

- DFS通常涉及到**递归**实现，本质上是使用了**编译栈**的原理。（非递归实现也可以完成DFS，使用一个栈来维护搜索过程即可，但代码的变式很多）

- BFS通常需要使用一个**队列**来维护搜索过程。

## 2.1 200. Number of Islands[medium]

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

**Example 1:**

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Example 2:**

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

 

**Constraints:**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.



### **遵循上下左右的顺序**

![image-20220910114947191](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220910114947191.png)



![image-20220910114620040](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220910114620040.png)

**思考**：1.什么时候岛屿计数 2.如何排除搜索过的位置

- 目标是找到矩阵中 “岛屿的数量” ，上下左右相连的 1 都被认为是连续岛屿。

- **dfs方法**： 设目前指针指向一个岛屿中的某一点 (r, c)，寻找包括此点的岛屿边界。

- 从 (r, c) 向此点的上下左右 (r+1,c),(r-1,c),(r,c+1),(r,c-1) 做深度搜索。
  终止条件：

  - (r, c) 越过矩阵边界;

  - **grid[r][c]**，代表此分支已越过岛屿边界。 搜索岛屿的同时，执行 grid[r][c]= '0'，即将岛屿所有节点删除，以免之后重复搜索相同岛屿。

    主循环：
    遍历整个矩阵，当遇到grid[r][c]== '1' 时，从此点开始做深度优先搜索 dfs，岛屿数 island + 1 且在深度优先搜索中删除此岛屿。
    最终返回岛屿数island即可。

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0]) ##初始化行列

        def dfs(grid, r, c): ##定义dfs函数
            if not 0 <= r < m or not 0 <= c < n or grid[r][c] == "0":##If it's outside the bounds or if it's traversing an element that's 0
                return
            grid[r][c] = "0" ## Modifies the traversed element to 0
            dfs(grid, r + 1, c) 
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)

        island = 0 ## Initialize the number of islands
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1": ##如果遍历到1，调用dfs函数并加岛屿数量
                    dfs(grid, r, c)
                    island += 1
        return island
```

```python
##BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        m = len(grid)
        n = len(grid[0])
        
        def bfs(i,j):

            queue = [[i, j]]
            queue.append((i,j))
            grid[i][j] = "0"

            while queue:
                (i,j) = queue.pop(0)
                ## 注意这里不可以grid[x][y] = "#" 因为

                for (x,y) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == "1":
                        queue.append((x,y))
                        grid[x][y] = "0"   ##把append 视为遍历了这个元素 否则可能会造成重复遍历元素的困境
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i,j)
                    island +=1 
        
        return island
```



## DFS图的模版

先上岛屿问题的DFS模板
r行坐标，c列坐标
0 —— 海洋格子
1 —— 陆地格子（未遍历过）
2 —— 陆地格子（已遍历过）

```python
def dfs(grid,r,c):
    if not 0<=r<len(grid) or not 0<=c<len(grid[0]):return #越界，直接返回

    if grid[r][c]!=1:return #不是陆地，直接返回

    grid[r][c]=2            #将遍历过的陆地标记为2，避免重复遍历

    dfs(grid,r-1,c)         #dfs上下左右的邻居节点（参考二叉树的dfs）
    dfs(grid,r+1,c)
    dfs(grid,r,c-1)
    dfs(grid,r,c+1)
```





### BFS图的模板

```python
bfs算法中的组成:
  1. viz = set()
    两个目的
    1.为了剪枝 减少跑的时间 (注意这里不需要set也是可以做到最短路径)
    2.为了避免重复遍历
   
  2. 数据结构用queue = []   ##有时候用tuple 来表示元素的坐标和这个元素的值 比如 (row,col, count)
  
  3. 遍历四个方向 for x,y in [(row+1,col), (row,col+1), (row-1,col-1), (row+1,col+1)]
 

模板:
  row = len(grid/matrix/..)
  col = len(grid[0]/matrix[0]/...)
  
  #建立 set
  viz = set()
  
  #建立queue
  queue = []
  
  
  #遍历
  for ...
    for ...
      满足条件加入queue
  
  #遍历queue中每一个元素
  while queue:
  
  #对queue的每一层进行发展 这里的每一层默认为四个角度 如果在tree里面的话为 同一层的每一个node
  for x,y in [(row+1,col), (row,col+1), (row-1,col-1), (row+1,col+1)]:
    目标元素满足matrix/grid的条件限制 且 满足其他条件eg: 不在viz...
      queue加入目标元素
      viz加入目标元素
```





