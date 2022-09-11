# 1. 堆的定义

堆是具有以下性质的完全二叉树：每个结点的值都大于或等于其左右孩子结点的值，称为大顶堆；或者**每个结点的值**都**小于**或等于其**左右孩子结点**的值，称为**小顶堆**（一般升序采用大顶堆，降序采用小顶堆)



![image-20220903155002628](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220903155002628.png)

**大顶堆：arr[i] >= arr[2i+1] && arr[i] >= arr[2i+2]**  

**小顶堆：arr[i] <= arr[2i+1] && arr[i] <= arr[2i+2]** 



# 2. python中的heapq库

python中的heapq库只有最小堆，没有最大堆，当使用最大堆时，可以在插入元素时将元素取反，弹出是也取反，一些常用操作如下：

```python

import heapq
# [2,0,4,1]
 
# 1.创建堆
# 方法一：定义一个空列表，然后使用heapq.heqppush(item)函数把元素加入到堆中
item = 2
heap = []
heapq.heappush(heap,item)
# 方法二：使用heapq.heapify(list)将列表转换为堆结构
heap = [2,0,4,1]
heapq.heapify(heap)
 
# 2.heapq.heappush() 添加新元素 num
num = 3
heapq.heappush(heap,num)
 
# 3.heapq.heappop() 删除并返回堆顶元素
heapq.heappop(heap)
 
# 4.heapq.heappushpop() 比较添加元素num与堆顶元素的大小:如果num>堆顶元素，删除并返回堆顶元素，然后添加新元素num;如果num<堆顶元素，返回num，原堆不变
# 其实也就等价于 添加新元素num，然后删除并返回堆顶元素
num = 0
heapq.heappushpop(heap,num)
 
# 5.heapq.heapreplace() 删除并返回堆顶元素，然后添加新元素num
num = 5
heapq.heapreplace(heap,num)
 
# 6. heapq.merge() 合并多个排序后的序列成一个排序后的序列， 返回排序后的值的迭代器。
heap1 = [1,3,5,7]
heap2 = [2,4,6,8]
heap = heapq.merge(heap1,heap2)
print(list(heap))
 
# 7.heapq.nsmallest() 查询堆中的最小n个元素
n = 3
heap = [1,3,5,7,2,4,6,8]
print(heapq.nsmallest(n,heap)) # [1,2,3]
 
# 8.heapq.nlargest() 查询堆中的最大n个元素
n = 3
heap = [1,3,5,7,2,4,6,8]
```



# 3. heap的特点

- min heap(最小堆)的root是最小值，

- 二叉堆是完全二叉树

- 找最值的time complexity是O(1) 因为只需要访问root

- insert/pop需要log(n)

  ![image-20220903172519194](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220903172519194.png)

  

