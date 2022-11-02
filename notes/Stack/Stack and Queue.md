## 1. 基础知识

**stack(Last in First Out)**,后进先出的数据结构，元素从栈的顶端入栈，然后从栈顶端出栈。进行删除操作时，【最后】入栈的元素离开栈。【栈底元素】的索引为0。

**queue(First in FIrst Out)**，先进先出的数据结构，元素从队列的后端入队，然后从队列前端出队。进行删除操作时，【最先】入队的元素离开队列。【队头元素】的索引为0。

## 2. 栈的基本操作

![image-20221101095058399](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20221101095058399.png)

![image-20221101095107713](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20221101095107713.png)

| 实现结构 | 入栈O(1)  | 出栈O(1) | 得到栈顶元素O(1) | 得到栈底元素O(1) |    是否为空     |
| :------: | :-------: | :------: | :--------------: | :--------------: | :-------------: |
|   list   | append(x) |  pop()   |    Stack[-1]     |     Stack[0]     | len(stack) == 0 |

```python
nums = [1,2,3,4]
##pop()删除队列末尾元素，即弹出栈顶元素
nums.pop() ##[1, 2, 3]
##得到栈底元素O(1)
print(nums[0])## 1
##得到栈顶元素O(1)
print(nums[-1]) ## 3
##把元素5加入栈顶
nums.append(5)
print(nums)  ##[1, 2, 3, 5]
```

