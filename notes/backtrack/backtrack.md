# Backtrack(回溯)

## 1. 回溯的定义



- **回溯：一种通过不断向前探索可能的候选解来找到问题解的方法**

- 回溯算法的思维过程

  - 建立问题模型和决策树
  - 在决策树上进行深度优先搜索（DFS），并使用剪枝进行优化

- 回溯算法包含的部分

  - **选择**----我可以做出的选择有哪些？
  - **限制条件**----有哪些选择是不可行的？
  - **结束条件**----在什么情况下可以得到问题的解？

  

<<<<<<< HEAD
## 2. 回溯的模版
=======
## 1. 回溯的模版
>>>>>>> 888632fb341394eaa1b205b7e0b3f38cd5ae2c72

```python
模板:
  result = []
  
  def backatrack(当前路径, 选择列表/当前的对象):
    if 满足结束条件:
      result.add(路径)
      return 
    
    for 选择 in 选择列表:
      做选择
      更新状态
      backtrack(路径, 选择列表)
      撤销选择（回滚）
```

![image-20220911155513292](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220911155513292.png)

<<<<<<< HEAD




## 3. 组合类问题



### 77. Combinations [medium]

Given two integers `n` and `k`, return *all possible combinations of* `k` *numbers chosen from the range* `[1, n]`.

You may return the answer in **any order**.

**Example 1:**

```
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
```

**Example 2:**

```
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
```

**Constraints:**

- `1 <= n <= 20`
- `1 <= k <= n`

**Ans**: 

1. 选择：所有范围内的数字

2. 限制条件：不能重复选取

3. 终止条件：满足k个数字

   确定递归函数包含哪些参数，返回什么参数。
   确定向内递归的终止条件，此处为临时结果数组path长度变为2，即认为需要将path中的结果加入到res中，此处返回。
   确定每一层的递归逻辑，每一层是一个for循环加上一个向内递归的入口，通过2中的终止条件来判定一共需要递归多少层，注意回溯和递归的差异就在于，回溯需要弹出之前的结果，来确保可以换到另外的路径上，不然会陷入死循环。

   **剪枝**

   根据本题题意，只需要每次取两个数，所以在逐渐搜索到4开头的数字的时候其实就没有继续向下搜索的必要了，所以此处在for循环到4作为开头的时候，需要进行剪枝处理。

   判定标准为i > n-(k-len(self.path))+1

   其中i为当前的处理数字，k-len(self.path)为距离结果还有多少个位置。

   假设此时path为空，则k-len(self.path)为2-0=2，意思为path中还可以放两个数，n-(k-len(self.path))+1结果为4-2+1=3，说明此时选择只能从123中选，最大不能超过3，因为是按顺序进行逐一组合，如果path为0的时候放入4，则必然得不到结果，4也就不考虑了；

   同理如果假设path为1，则根据相应运算得到此时结果为4，则此时意味着最后一位元素放1234都是可以的。

   此题剪枝效果还没有很明显，只是去除了4作为开头的一个小情况，但是也得到了一定的运行时间缩短。


```python

```

=======
>>>>>>> 888632fb341394eaa1b205b7e0b3f38cd5ae2c72
