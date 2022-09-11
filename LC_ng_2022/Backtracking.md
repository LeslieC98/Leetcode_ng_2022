# 回溯(backtracking)

## 1. 什么是回溯

- 回溯是一种暴力穷举算法

- 穷举过程是遍历一颗多叉树的过程

- 回溯算法和多叉树遍历代码框架类似

  

  回溯算法和我们常说的 DFS 算法非常类似，本质上就是一种暴力穷举算法。回溯算法和 DFS 算法的细微差别是：**回溯算法是在遍历「树枝」，DFS 算法是在遍历「节点」**

  

  解决一个回溯问题，实际上就是一个决策树的遍历过程，站在回溯树的一个节点上，你只需要思考 3 个问题：

  1、路径：也就是已经做出的选择。

  2、选择列表：也就是你当前可以做的选择。

  3、结束条件：也就是到达决策树底层，无法再做选择的条件。

  ```python
  result = []
  def backtrack(选择列表, 路径):
      if 满足结束条件:
          result.add(路径)
          return
  
      for 选择 in 选择列表:
          # 做选择
          路径.add(选择)
          将该选择从选择列表移除
          backtrack(选择列表, 路径) # 核心 递归调用之前【做选择】，调用之后【撤销选择】
          # 撤销选择
          路径.remove(选择)
          将该选择再加入选择列表
  
  
  ```

  **其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」**



## 2. 回溯经典例题



###  46.  Permutations

Given an array `nums` of distinct integers, return *all the possible permutations*. You can return the answer in **any order**.

**Example 1:**

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Example 2:**

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

**Example 3:**

```
Input: nums = [1]
Output: [[1]]
```



#### Ans:

#### 元素无重不可复选

以[1,2,3]为例，抽象成树形结构如下:

![46.全排列](https://code-thinking-1253855093.file.myqcloud.com/pics/20211027181706.png)

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # 选择列表就是nums包含的元素
        # 使用used标记已经选择的数字 间接表示选择列表的变化
        visited = [False]*len(nums)
        def backtrack(nums, path, visited):
            # 结束条件
            if len(path) == len(nums):
                res.append(path[:]) # ！！！此处有坑需要注意
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    # nums[i]已经选过 跳过
                    continue
                # 做选择
                path.append(nums[i])
                visited[i] = True # 更新选择列表
                # 递归
                backtrack(nums, path, visited)##回去上一层
                # 撤销选择
                visited[i] = False
                path.pop()
                # 回退选择列表的变化

        # 初始时路径为空，所有元素都没有选择过所以used中都是False
        backtrack(nums,[],visited)
        return res
```





### 47.  Permutations II



Given a collection of numbers, `nums`, that might contain duplicates, return *all possible unique permutations **in any order**.*

**Example 1:**

```
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
```

**Example 2:**

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```



#### Ans：

这道题目和[46.全排列 (opens new window)](https://programmercarl.com/0046.全排列.html)的区别在与**给定一个可包含重复数字的序列**，要返回**所有不重复的全**排列****

**还要强调的是去重一定要对元素进行排序，这样我们才方便通过相邻的节点来判断是否重复使用了**。

![47.全排列II1](https://img-blog.csdnimg.cn/20201124201331223.png)

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)
        nums.sort()##为什么加了这步就可以了,排序
        
        

        def backtrack(nums, path, visited):
            if len(nums) == len(path):
                return res.append(path[:])
            
            for i in range(0,len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:##如果一个数和前一个数相同且没有被记录，继续循环（1，1，2）
                    continue
                if not visited[i]:
                    path.append(nums[i])
                    visited[i] = True
                    backtrack(nums,path, visited)
                    path.pop()
                    visited[i] = False
 
        backtrack(nums,[],visited)

        return res   
```

