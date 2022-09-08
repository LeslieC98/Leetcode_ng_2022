## Set and Dictionary

### set

![image-20220718151542846](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220718151542846.png)

![image-20220718151821645](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220718151821645.png)



#### set常见操作

- Create: add, update
- Read: integration, in
- Delete: remove, clear, discard, pop
- 其他：len

#### Python 大括号代表集合set和dic

```python
#大括号定义字典
set_2 = {12, 15, 18.2, 'hello'}
#增
set_1.add('Jiuzhang')##插入一个元素
set_1.update([11, 'abc']) ##批量插入列表
#查
for i in set_1:
  print(i, end = ' ')
12 in set_1 #时间复杂度O(1)
#删
if i(元素) in set_1:
  set_1.remove()##要进行是否在集合里的判断
set_1.discard()##无论元素是否在集合中，都删除
set_1.pop()##直接随机删除元素并返回，一般不用
#查找元素个数
len(set_1)
#union(并集)
set_2.union(set_3)
set_2 | set_3
#交集
set_2 & set_3
```



#### Set非常适合记录某元素是否出现过（插入查找都是O(1),效率非常高)



#### <u>26. Remove Duplicates from Sorted Array</u>

https://leetcode.com/problems/remove-duplicates-from-sorted-array/



### Dictionary

![image-20220718204422918](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220718204422918.png)

```python
dict_2 = {'spam': 2, 'eggs': 3, 'food': {'ham': 1, 'ice': 2}}##字典是非重复key的健值对

#create
dic_2[2] = 4

#read
if 'jiuzhang' in dict_1:
    print(dict_1['jiuzhang'])

dict_1.get('jiuzhang', 0) #get()方法可以返回指定键的值，如果该键不存在的话，返回默认值0
dict_1.keys()
dict_1.values()
dict_1.items()

#迭代遍历
for key in dict_2:
    print(key, dict_2[key])

#update
dict_1['jiuzhang'] = 100
dict_1

#delete
dict_2.pop('spam')
dict_2

#len
len(dict_2)
```

![image-20220720232418015](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220720232418015.png)

- dict可以查找元素的位置和值



![image-20220720232837196](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220720232837196.png)

list不能放入set也不能用作dict的key



![image-20220720233047005](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220720233047005.png)

![image-20220720234003743](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220720234003743.png)

![image-20220720234039854](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220720234039854.png)

![image-20220720234139790](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220720234139790.png)

![image-20220720234506747](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220720234506747.png)

![image-20220720234525091](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220720234525091.png)

![image-20220720235201782](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220720235201782.png)

![image-20220720235242840](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220720235242840.png)

![image-20220720235320575](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220720235320575.png)

![image-20220720235343451](/Users/lesliecheung/Library/Application Support/typora-user-images/image-20220720235343451.png)

