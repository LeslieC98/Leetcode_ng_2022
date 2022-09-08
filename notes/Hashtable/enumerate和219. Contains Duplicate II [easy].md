# 1. enumerate()函数的用法

enumerate()是python的内置函数，在字典上是枚举、列举的意思，**多用于在for循环中得到计数，利用它可以同时获得索引和值，**即需要**index和value值**的时候可以使用enumerate



```python
##enumerate的使用：
例如：已知s = [1,2,3,4,5,6]，要求输出:
0,1
1,2
2,3
3,4

s = [1, 2, 3, 4]
e = enumerate(s)
for index, value in e:
    print('%s, %s' % (index, value))
    
输出结果：
0, 1
1, 2
2, 3
3, 4

s = [1, 2, 3, 4]
# 从指定索引1开始
for index, value in enumerate(s, 1):
    print('%s, %s' % (index, value))
 
输出结果：
1, 1
2, 2
3, 3
4, 4
```



# 219. Contains Duplicate II 

Given an integer array `nums` and an integer `k`, return `true` if there are two **distinct indices** `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

 

**Example 1:**

```
Input: nums = [1,2,3,1], k = 3
Output: true
```

**Example 2:**

```
Input: nums = [1,0,1,1], k = 1
Output: true
```

**Example 3:**

```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

 

**Constraints:**

- `1 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`
- `0 <= k <= 105`



## 解法1: Hashtable and Dic

```python
##time complexity O(n)
##space complexity O(n)

1.利用dic 的key唯一而值不为一的特点利用enumerate()把索引作为值，数组的值作为索引存储到dic里，并通过：
if value in dic and (index - dic[value] <= k): 如果数组的值在之前已经存在于dic中（key存在），
且abs(i-j)<=k <=> 当前索引-之前索引 <= k 

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for index, value in enumerate(nums): ##{3:1}
            if value in dic and (index - dic[value] <= k): ### {index == 3 and dic[value]= dic[1] ==0 3-0<=k
                return True
            dic[value] = index ##{1:0,2:1,3:2}
        return False
```



## 解法 2: Sliding Window

维护一个存在**k个元素的窗口**，先判断遍历到的元素之前是否**在窗口内**，如果**之前**在窗口内出现，返回True，如果没有，窗口中第一个元素，并将该元素加入

```python
##time complexity O(n)
##space complexity O(k)

# 方法2：滑动窗口
# 方法1的改良版，即维护一个存在k个元素的窗口，此时与方法1不同的是，不用再记录nums中某个数最近一次出现的下标，
# 因为在窗口中的元素的下标必定满足要求，只需要判断是否有重复即可，因此使用元组，而无需再使用字典
# 每当遍历到下一个元素时，先判断其是否在窗口内，若不在，则删除窗口中第一个元素，并将该元素加入
# nums = [1,2,3,1] k =2
# 当遍历到3时
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if k == 0:
            return False
        win = set()
        for i, num in enumerate(nums): ##将{2:3}放入win() {1,2}中
            if num in win:
                return True
            elif i < k:  ##2=k
                win.add(num)
            else:  
                win.remove(nums[i - k]) ##remove nums[2-2]也就是第一个
                win.add(nums[i])
        return False
```

**也可以不用enumerate**

遍历数组所有元素，使用哈希集合 set 作为滑动窗口容器存储数组中连续的 **k 个元素**，**索引 i 大于 k 之后需要剔除滑动窗口容器的首个元素 nums[i - k - 1] 以保证其长度不超过 k**，如果当前元素已存在于哈希集合则说明二者索引差值不大于 k 应返回 true，遍历结束仍未找到符合条件的数字则返回 falsew

如果 i > ki>k，则下标 i−k−1 处的元素被移出滑动窗口，因此将nums[i - k - 1] 从哈希集合中删除；

判断 nums[i] 是否在哈希集合中，如果在哈希集合中则在同一个滑动窗口中有重复元素，返回 true，如果不在哈希集合中则将其加入哈希集合。

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        win = set()
        for i in range(len(nums)):         
            if i > k:
                win.remove(nums[i-k-1])
            if nums[i] in win:
                return True 
            win.add(nums[i])
        return False
```

