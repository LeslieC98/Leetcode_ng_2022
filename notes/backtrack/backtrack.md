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

  

## 1. 回溯的模版

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

