# Python的一些函数



### 1. sorted

#### 1.1 sort 与 sorted 的区别：

sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作

#### 1.2 sorted 语法：

```python
sorted(interable, key = None, reverse = False)
```

- iterable – 可迭代对象。
- key – 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
- reverse – 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

#### 1.3 sorted() 函数与 lambda 表达式结合

##### 按照二维矩阵下标为 1 的列进行排序

```python
matrix = [[7,0], [4,4], [7,11, [5,0], [6,11, [5,21]
ret= sorted (matrix, key=lambda x: x[1])
print(ret)
##输出
[[7, 0], [5, 0], [7, 1], [6, 1], [5, 2], [4, 4]]
```



### 2. setdefault



### 3. collections.Counter

Counter 计数器，顾名思义就是用来计数的，最主要的作用就是计算**“可迭代序列中”各个元素（element）的数量。**

#### 3.1 引入方法

```python
from collections import Counter
```

#### 3.2 对字符串和列表的作用

```
#对列表
list_01 = [1,9,9,5,0,8,0,9] #GNZ48-陈珂生日
print (Counter(list 01)) Counter({9: 3, 0: 2, 1: 1, 5: 1, 8: 1})

#对字符串作用
from collections import Counter
temp = Counter('abcabcababcde')
print(temp) ##Counter({'a': 4, 'b': 4, 'c': 3, 'd': 1, 'e': 1})


#以上甘实是两种使用方法
一种是直接用，一种是实例化以后使用，如果要频繁调用的话，显然后一种更简洁
```

#### 3.3 输出结果

```

#查看类型
print( type(temp) ) #<class 'collections.Counter'>
 
#转换为字典后输出
print( dict(temp) ) #{'b': 4, 'a': 5, 'c': 3, 'd': 2, 'e': 1}
 
for num,count in enumerate(dict(temp).items()):
    print(count)
"""
('e', 1)
('c', 3)
('a', 5)
('b', 4)
('d', 2)
"""

```

#### 3.4 计算元素总数，Keys()&Values()

```python
from collections import Counter
 
c = Counter('ABCABCCC')
print(sum(c.values()))  # 8  total of all counts
 
print(c.keys())  #dict_keys(['A', 'B', 'C'])
print(c.values())  #dict_values([2, 2, 4])
```



#### 4. Items(), key(), value()

这 3 个方法之所以放在一起介绍，是因为它们都用来获取字典中的特定数据。keys() 方法用于返回字典中的所有键；values() 方法用于返回字典中所有键对应的值；items() 用于返回字典中所有的键值对。

```python
a = {'数学': 95, '语文': 89, '英语': 90}
print(a.keys())
print(a.values())
print(a.items())
```

结果：

```python
dict_keys(['数学', '语文', '英语'])
dict_values([95, 89, 90])
dict_items([('数学', 95), ('语文', 89), ('英语', 90)])
```

```python
a = {'数学': 95, '语文': 89, '英语': 90}
for key, value in a.items():
    print(key,value)
    ##数学 95语文 89英语 90
```

